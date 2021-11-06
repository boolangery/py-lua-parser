import sys
from optparse import OptionParser, OptionGroup
import luaparser
from luaparser import ast
from luaparser.builder import SyntaxException


def abort(msg):
    sys.stderr.write(msg + "\n")
    sys.exit()


def main():
    # parse options:
    parser = OptionParser(
        usage="usage: %prog [options] file|directory",
        version="%prog " + luaparser.__version__,
    )
    cli_group = OptionGroup(parser, "CLI Options")
    cli_group.add_option(
        "-s",
        "--source",
        metavar="F",
        type="string",
        dest="source",
        help="source passed in a string",
    )
    cli_group.add_option(
        "-x",
        "--xml",
        action="store_true",
        dest="xml",
        help="set output format to xml",
        default=False,
    )
    cli_group.add_option(
        "--pretty",
        action="store_true",
        dest="pretty",
        help="set output format to python ast pretty print style",
        default=False,
    )
    cli_group.add_option(
        "-o",
        "--output",
        metavar="F",
        type="string",
        dest="output",
        help="write output to file",
    )
    parser.add_option_group(cli_group)

    (options, args) = parser.parse_args()

    # check argument:
    if not options.source and not len(args) > 0:
        abort("Expected a filepath")

    try:
        if options.source:
            tree = ast.parse(options.source)
        else:
            with open(args[0], "r") as content_file:
                content = content_file.read()
            tree = ast.parse(content)

        # output format
        if options.pretty:
            output = ast.to_pretty_str(tree)
        elif options.xml:
            output = ast.to_xml_str(tree)
        else:
            output = ast.to_pretty_json(tree)

        # output
        if options.output:
            with open(options.output, "w") as content_file:
                content_file.write(output)
        else:
            print(output)
    except SyntaxException as e:
        print("error: " + str(e))


if __name__ == "__main__":
    main()
