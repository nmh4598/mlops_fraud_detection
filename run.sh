#!/bin/bash

API_ENDPOINT="http://0.0.0.0:8000"

platform(){
    if [ $1 == "up" ]; then
        docker-compose -f ./deployment/docker-compose.yaml up -d
    elif [ $1 == "down" ]; then
        docker-compose -f ./deployment/docker-compose.yaml down
    fi
}

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

help() {
    echo "Usage: run.sh <command>"
    echo
    echo "Available commands:"
    echo "  platform up      - Deploy all necessary services like fastapi, grafana, mlflow and postgresql using Docker Container"
    echo "  platform down    - Stop all services using Docker Compose"
    echo "  test             - Run unit tests for the running FastAPI API"
    echo "  git-push <args>  - Commit and push changes to a Git branch, semantic and coding style will be checked before pushing code"
}


if [ "$1" == "test" ]; then
    # Execute the test function
    test
elif [ "$1" == "git-push" ]; then
    # Remove the "git-commit" argument before passing to the commit function
    shift
    # Execute the commit function
    push "$@"
elif [ "$1" == "platform" ]; then
    # Remove the "git-commit" argument before passing to the commit function
    shift
    # Execute the commit function
    platform "$@"
elif [ "$1" == "help" ]; then
    # Display help information
    help
else
    # Invalid command, display usage instructions
    help
fi