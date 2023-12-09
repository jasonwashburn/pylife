import sys
from argparse import Namespace

from pylife import patterns, views
from pylife.cli import get_command_line_args


def main() -> None:
    args = get_command_line_args()
    view = getattr(views, args.view)
    if args.all:
        for pattern in patterns.get_all_patterns():
            _show_pattern(view, pattern, args)
    else:
        _show_pattern(
            view,
            patterns.get_pattern(name=args.pattern),
            args,
        )


def _show_pattern(view, pattern: patterns.Pattern, args: Namespace) -> None:
    try:
        view(pattern=pattern, gen=args.gen, frame_rate=args.fps).show()
    except Exception as error:
        print(error, file=sys.stderr)


if __name__ == "__main__":
    main()
