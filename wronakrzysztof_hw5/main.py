try:
    import github.repository
    import logging
    import os.path
    import argparse
except Exception as e:
    print("Seems like some modules are missing. Please read INSTALL.md")
    print("Exception says: ", e)
    raise SystemExit

def main():
    """
    Main function, initiates logger and parser. Then creates repository based on parsed arguments.
    :return:
    """
    authentication = ('krzychuwr1', '18f8c2afdb7504a1fe6b914eb8b9669528b81bba')
    logging.basicConfig(filename=os.path.join('logs', 'main.log'), level=logging.DEBUG, format='%(asctime)s %(message)s')

    logging.info("Program has started.")

    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Username in github")
    parser.add_argument("repository", help="Name of repository in github")
    args = parser.parse_args()

    print("\nDownloading repository:", args.repository, "from user",  args.username, ".")
    print("This may take a while.")

    try:
        repository = github.repository.Repository(authentication)
        logging.info("Repository object has been created successfully.")
    except Exception as e:
        handle_exception(e, "Couldn't create a repository object.")
        return

    try:
        repository.get_repository(args.username, args.repository)
        logging.info("Repository data has been successfully retrieved.")
    except Exception as e:
        handle_exception(e, "Couldn't retrieve repository data.")
        return

    try:
        for key, file in repository.files.items():
            print("file:", file.name)
            file.count_score()
            print("Score: ", file.score, "\n")
        logging.info("Result has been printed successfully")
    except Exception as e:
        handle_exception(e, "Couldn't print the results")
        return


def handle_exception(e, log):
        logging.critical(log)
        logging.critical(e)
        print("An error has occured.")
        print("Check the logs for more information.")

try:
    main()
except KeyboardInterrupt:
    print("Bye bye")
