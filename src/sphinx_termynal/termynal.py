from importlib import resources
from pathlib import Path

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset


def _escape(txt: str) -> str:
    txt = txt.replace("&", "&amp;")
    txt = txt.replace("<", "&lt;")
    txt = txt.replace(">", "&gt;")
    txt = txt.replace('"', "&quot;")
    return txt  # noqa:RET504


class TermynalDirective(SphinxDirective):
    has_content = True

    def run(self):  # type: ignore
        content = (
            '<div class="termy" data-termynal data-ty-macos data-ty-title="bash">\n'
        )
        input_continue = False
        for line in self.content:
            line = line.strip()
            eline = _escape(line)
            if line.startswith("$"):
                content += f'<span data-ty="input">{eline[1:]}</span>\n'
                input_continue = line.endswith("\\")
            elif line.startswith("-->"):
                content += '<span data-ty="progress"></span>\n'
            elif input_continue:
                content += (
                    f'<span data-ty="input" data-ty-prompt="&gt;"> {eline}</span>\n'
                )
                input_continue = line.endswith("\\")
            else:
                content += f"<span data-ty>{eline}</span>\n"
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
