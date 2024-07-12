# sporty_challenge_1
This repository contains the first QA challenge development

## Repository Structure
For this project, a Page Objects Pattern was used.

In the src folder, there are subfolder that contains specific parts to be used in the project.

The src folder contains three sub folders, which are:

- common: contains the functions that can be shared among tests.
- pages: contains the selectors used in the tests. Each page has its own selectors.
- setup: contains the functions that setup the environment/browser.

The test folder contains all the tests belonging to the project.

## Test Case
    - Go to twitch.tv
        - Close the cookies modal
    - Click in the search icon
    - Input StarCraft II
    - Scroll down twice
    - Select one streamer
        - Close classification gate pop-up if displayed
    - Take a screenshot after streamer page is loaded


## Test Run GIF
As requested, below, one can find the test run GIF:

<img src="1-test_run_recorded.gif" width="250" height="500">

## Additional Test Case
    - Go to a streamer page that has the classification gate
        - Close the cookies modal
    - Close classification gate pop-up if displayed

## Additional Test Run GIF
Below, one can find the test run GIF:

<img src="2-additional_test_run_recorded.gif" width="250" height="500">