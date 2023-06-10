#!/bin/bash

API_ENDPOINT="http://0.0.0.0:8000"

test() {
    # Check if the server at API_ENDPOINT is running using "curl"
    # If yes, run `pytest tests/`
    # If no, print error message
    if curl -s $API_ENDPOINT > /dev/null; then
        pytest tests/
        return $?
    else
        echo "You need to initiate the platform first, using 'run platform all up'"
        return 1
    fi
}

push() {
    # Execute flake8 and black before committing
    flake8 --exclude=__init__.py app
    if [ $? -ne 0 ]; then
        echo "Please resolve all the 'flake8' alerts before committing!"
        echo "'black' might automatically change the code and violate 'flake8', so check how 'black' formatted your code as well"
        return 1
    fi

    black --check --line-length 80 app
    if [ $? -ne 0 ]; then
        echo "Please resolve all the 'black' formatting issues before committing!"
        return 1
    fi

    # If there are no issues, proceed with the commit
    git push "$@"
}

# Check command-line arguments
if [ "$1" == "test" ]; then
    # Execute the test function
    test
elif [ "$1" == "git-push" ]; then
    # Remove the "git-commit" argument before passing to the commit function
    shift
    # Execute the commit function
    push "$@"
else
    # Invalid command, display usage instructions
    echo "Usage: run.sh [test | git-commit <commit_args>]"
fi
