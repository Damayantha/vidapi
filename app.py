import argparse
from sup import app

version = '0.5'
"""
    A server for providing the app anywhere, no need for GAE
"""

def main():
    desc = """
           The youtube-dl API server.
           """

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        '-p', '--port',
        default=9191,
        type=int,
        help='The port the server will use. The default is: %(default)s',
    )

    parser.add_argument(
        '--host',
        default='localhost',
        type=str,
        help='The host the server will use. The default is: %(default)s',
    )

    parser.add_argument(
        '--threaded',
        action='store_true',
        help='Run the server with threading enabled. Cannot be used with --number-processes.',
    )

    parser.add_argument(
        '--number-processes',
        default=None,
        type=int,
        help='The number of processes the server will use. Cannot be used with --threaded.',
    )

    parser.add_argument('--version', action='store_true',
                        help='Print the version of the server')

    args = parser.parse_args()

    if args.version:
        print(version)
        exit(0)

    if args.threaded and args.number_processes is not None:
        parser.error("Cannot use --threaded and --number-processes together.")

    if args.threaded:
        app.run(host=args.host, port=args.port, threaded=True)
    elif args.number_processes is not None:
        app.run(host=args.host, port=args.port, processes=args.number_processes)
    else:
        app.run(host=args.host, port=args.port)

if __name__ == "__main__":
    main()
