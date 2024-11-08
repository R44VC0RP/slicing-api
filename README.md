# slicing-api

Using prusa-slicer as an API for slicing 3D models and getting information about the final print.

prusa-slicer cli docs is exactly the same as slic3r cli docs.

Use `prusa-slicer --help-fff` to see the options for the print. I will feed this into claude to build an API that can control the command.

Each api request will spawn a thread that will run the command and return the output. It will be async so the initial request will return immediately with a job id. On completion it will POST the result to the callback url with the job id.