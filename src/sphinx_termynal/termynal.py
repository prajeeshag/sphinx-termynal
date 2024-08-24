from importlib import resources
from pathlib import Path

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset


class TermynalDirective(SphinxDirective):
    has_content = True

    def run(self):  # type: ignore
        content = (
            '<div class="termy" data-termynal data-ty-macos data-ty-title="bash">\n'
        )
        for line in self.content:
            line = line.strip()
            if line.startswith("$"):
                content += f'<span data-ty="input">{line[1:]}</span>\n'
            elif line.startswith("-->"):
                content += '<span data-ty="progress"></span>\n'
            else:
                content += f"<span data-ty>{line}</span>\n"
        content += "</div>\n"
        raw_html_node = nodes.raw("", content, format="html")
        return [raw_html_node]


def copy_static_files(app: Sphinx, exception: Exception | None):
    if exception is None:  # Make sure the build process was successful
        with resources.as_file(
            resources.files(__package__).joinpath("static")
        ) as static_dir:
            static_target_dir = Path(app.outdir) / "_static"
            copy_asset(str(static_dir), str(static_target_dir))


def setup(app: Sphinx):  # type: ignore
    app.add_directive("termynal", TermynalDirective)
    app.add_css_file("termynal.css")
    app.add_js_file("termynal.js", loading_method="defer")
    app.connect("build-finished", copy_static_files)  # type: ignore
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
