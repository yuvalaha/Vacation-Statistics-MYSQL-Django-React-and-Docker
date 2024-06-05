from datetime import datetime
from flask import session


class Logger:

    # Path to log file:
    __log_file = "./logger.log"

    # Save log message:
    @staticmethod
    def log(message):
        # Take current time:
        now = datetime.now()
        # Open file:
        with open(Logger.__log_file, "a") as file:  # "a" = Append
            # Write time:
            file.write(str(now) + "\n")
            # Write message:
            file.write(str(message) + "\n")
            # Write user data if exist:
            user = session.get("user")
            if user:
                file.write(
                    "User ID: " + str(user["user_id"]) + ", User Email: " + user["email"] + "\n")
            # Write separator:
            file.write(
                "-----------------------------------------------------------------\n")
