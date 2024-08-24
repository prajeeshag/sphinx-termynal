# type: ignore
from pathlib import Path

import pytest
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import new_document

from sphinx_termynal.termynal import (
    TermynalDirective,
    copy_static_files,
)


@pytest.fixture
def document():
    settings = {}
    document = new_document("test_doc", settings)
    return document


@pytest.mark.parametrize(
    "content, expected_html",
    [
        (
            ['$ > < & " '],
            (
                '<div class="termy" data-termynal data-ty-macos data-ty-title="bash">\n'
                '<span data-ty="input"> &gt; &lt; &amp; &quot;</span>\n'
                "</div>\n"
            ),
        ),
        (
            [
                "$ pip install \\",
                "sphinx-termynal \\",
                "another_package",
                "-->",
                "Done",
            ],
            (
                '<div class="termy" data-termynal data-ty-macos data-ty-title="bash">\n'
                '<span data-ty="input"> pip install \\</span>\n'
                '<span data-ty="input" data-ty-prompt="&gt;"> sphinx-termynal \\</span>\n'
                '<span data-ty="input" data-ty-prompt="&gt;"> another_package</span>\n'
                '<span data-ty="progress"></span>\n'
                "<span data-ty>Done</span>\n"
                "</div>\n"
            ),
        ),
        (
            ["$ pip install \\", "sphinx-termynal", "-->", "Done"],
            (
                '<div class="termy" data-termynal data-ty-macos data-ty-title="bash">\n'
                '<span data-ty="input"> pip install \\</span>\n'
                '<span data-ty="input" data-ty-prompt="&gt;"> sphinx-termynal</span>\n'
                '<span data-ty="progress"></span>\n'
                "<span data-ty>Done</span>\n"
                "</div>\n"
            ),
        ),
    ],
)
def test_termynal_directive(mocker, content, expected_html):
    """Test the TermynalDirective output."""
    # Mock the state and state_machine
    state_machine = mocker.Mock()
    state_machine.reporter = mocker.Mock()
    # Create an instance of the directive
    directive = TermynalDirective(
        name="termynal",
        arguments=[],
        options={},
        content=content,
        lineno=1,
        content_offset=0,
        block_text="",
        state=None,
        state_machine=state_machine,
    )

    # Run the directive
    result = directive.run()

    # Check the raw HTML content
    raw_html_node = result[0]
    assert isinstance(raw_html_node, nodes.raw)
    assert raw_html_node.astext() == expected_html


def test_copy_static_files(tmpdir, mocker):
    """Test the copy_static_files function."""
    srcdir = tmpdir.mkdir("src")
    outdir = tmpdir.mkdir("out")
    tmpdir.join("conf.py").write("#")
    app = Sphinx(
        srcdir=str(srcdir),
        confdir=str(tmpdir),
        outdir=str(outdir),
        doctreedir=str(tmpdir),
        buildername="html",
    )
    exception = None

    # Create a fake static directory in the extension
    static_dir = tmpdir.mkdir("static")
    static_dir.join("termynal.css").write("/* CSS content */")
    static_dir.join("termynal.js").write("// JS content")

    # Mock the resources.as_file to return a mock context manager
    mock_as_file = mocker.MagicMock()
    mock_as_file.__enter__.return_value = static_dir
    mock_as_file.__exit__ = mocker.Mock(return_value=None)
    mocker.patch(
        "sphinx_termynal.termynal.resources.as_file", return_value=mock_as_file
    )

    # Call the function to copy static files
    copy_static_files(app, exception)

    # Verify that files were copied to the output directory
    static_target_dir = Path(app.outdir) / "_static"
    assert static_target_dir.exists()
    assert (static_target_dir / "termynal.css").exists()
    assert (static_target_dir / "termynal.js").exists()
    assert (static_target_dir / "termynal.css").read_text() == "/* CSS content */"
    assert (static_target_dir / "termynal.js").read_text() == "// JS content"


# @pytest.mark.sphinx("html", testroot="basic")
# def test_extension_integration(app, status, warning):
#     """Test full integration of the extension with Sphinx."""
#     app.builder.build_all()
#     status_iterator(app.env.found_docs, "testing ", "document")

#     # Check that the directive and assets are included in the build
#     assert "termynal.css" in app.builder.css_files
#     assert "termynal.js" in app.builder.script_files
#     assert (Path(app.outdir) / "_static" / "termynal.css").exists()
#     assert (Path(app.outdir) / "_static" / "termynal.js").exists()
