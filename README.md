
# Team: Teleos

# Problem Statment - Time and Productivity Analysis

## Proposed Solution 
In any company , employees are usually divided into certain domains in which ,based on their designation ,work is is allocated.
For example: A developer , should take the input (Uml Diagrams) from a software engineer , understand them and then develop a working
model.
However, it so happens that the often employees end up doing work outside their domain.Like the Developer in the above example, might end up documenting the solution instead of developing.Such deviations in the task field will lower the productivity and waste time and resources of the company The solution to avoid such strays is to use an application and track and store the activities and time taken of all the employees and based on this data we provide an analysis of why the aforementioned deviations occur and suggest what to do to avoid them.
## Implemenation Logic
The web app has two phases.
### Phase 1:
In the First phase , the team-leader or HR has to set up her/his account. To do so he/she needs to provide details regarding the company , such as Company Name, Number of employees,Number of Projects being worked on,The Services(tools) being used by the company(example: Slack,Excel sheets etc).
Once the app is logged into by the personnel , it will start to track the activity of all the employees previously entered.
The app checks what the employee is doing by tracking the systems monitor, key board and mouse.Then later the HR will be able to view the report generated in phase-2
### Phase 2:
This is the most important phase of the project.The data collected in the above stage(tracking) is stored in a centralized database.
On this data , we apply techniques of Data Analytics(like regression etc.) to generate a report for a stipulated time(week or month).
Based on this report , the organization can identify what are the factors causing the lowering of productivity and take decisions to rectify them.

## Future Enhancements
The following enhancements can be made to the present model to increase the efficiency and increase the scope of the application.
1.	Face detection and gaze tracking module to monitor the employee’s presence at all times.(Only used to alert the user
2.	Calculation of the CPU’s Utilization at every point of time to make sure that the employee is not sitting idle in front of the computer.
3.	A module that readily downloads the pdf version of the report at any instance.


## Packages Required

- Flask
- MySQLdb
- pynput
- win32gui
- pandas
- numpy


## How to Execute ?
Execute the flask_b file using the following command.

``` 
python flask_b.py

```
Copy and Paste the the link shown in a Web Browser. Make sure the server is running in the behind. 

## Supported OS
As of now the product only works on the windows and unix evnironment and not on MacOS.

Because of the security reasons of MacOS,the system is not allowing the module pynput to track the key and mouse events.we're working on the alternative module for the mac to track key and mouse events.
