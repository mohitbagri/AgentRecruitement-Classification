# AgentRecruitement-Classification

## Problem Statement 
Your client is a Financial Distribution company. Over the last 10 years, they have created an offline distribution channel across country. They sell Financial products to consumers by hiring agents in their network. These agents are freelancers and get commission when they make a product sale.

## Overview of your client On-boarding process
The Managers at your client are primarily responsible for recruiting agents. Once a manager has identified a potential applicant, the would explain the business opportunity to the agent. Once the agent provides the consent, an application is made to your client to become an agent. This date is known as application_receipt_date.
In the next 3 months, this potential agent has to undergo a 7 days training at the your client's branch (about Sales processes and various products) and clear a subsequent examination in order to become an agent.

The problem - Who are the best agents?
As is obvious in the above process, there is a significant investment which your cleint makes in identifying, training and recruiting these agents. However, there are a set of agents who do not bring in the expected resultant business.
Your client is looking for help from data scientists like you to help them provide insigths using their past recruitment data. They want to predict the target variable for each potential agent, which would help them identify the right agents to hire.

## Data

<!DOCTYPE html>
<html>
<body>
<table style="width:100%">
  <tr>
    <td>Variable</td>
    <td>Definition</td>
  </tr>
  <tr>
    <td>ID</td>
    <td>Unique Application ID</td>
  </tr>
  <tr>
    <td>Office_PIN</td>
    <td> PINCODE of Your client's Offices</td>
  </tr>
  <tr>
    <td>Application_Receipt_Date</td>
    <td>Date of Application</td>
  </tr>
  <tr>
    <td>Applicant_City_PIN</td>
    <td>PINCODE of Applicant Address</td>
  </tr>
  <tr>
    <td>PINCODE of Applicant Address</td>
    <td>PINCODE of Your client's Offices</td>
  </tr>
  <tr>
    <td>Applicant_Gender</td><td>	Applicant's Gender</td>
  </tr>
    <tr>
      <td>Applicant_BirthDate</td><td>	Applicant's Birthdate</td>
  </tr>
  <tr> 
    <td> Applicant_Marital_Status</td><td>	Applicant's Marital Status</td>
  </tr>
<tr>
  <td>Applicant_Occupation</td><td>	Applicant's Occupation</td>
 </tr>
 <tr> 
   <td>Applicant_Qualification</td><td>	Applicant's Educational Qualification</td>
  </tr>  
<tr>
  <td>Manager_DOJ</td><td>	Manager's Date of Joining</td>
</tr> 
<tr>
  <td>Manager_Joining_Designation</td><td>	Manager's Joining Designation</td>
  </tr>  
 <tr>
   <td>Manager_Current_Designation</td><td>	Manager's Designation at the time of application sourcing</td>
  </tr>
  <tr>
    <td>Manager_Grade</td><td>	Manager's Grade</td>
  </tr>
  <tr>
    <td>Manager_Status</td>	<td>Current Employment Status (Probation / Confirmation)</td>
  </tr>
  <tr>
    <td>Manager_Gender</td><td>	Manager's Gender</td>
  </tr>
 <tr> 
   <td>Manager_DoB</td><td>	Manager's Birthdate</td>
  </tr>
  <tr>
    <td>Manager_Num_Application</td><td>	No. of Applications sourced in last 3 months by the Manager</td>
  </tr>
  <tr>
    <td>Manager_Num_Coded</td><td>	No. of agents recruited by the manager in last 3 months</td>
  </tr>
  <tr>
    <td>Manager_Business</td><td>	Amount of business sourced by the manager in last 3 months</td>
  </tr>
  <tr>
    <td>Manager_Num_Products</td><td>	Number of products sold by the manager in last 3 months</td>
  </tr>
  <tr>
    <td>Manager_Business2</td><td>	Amount of business sourced by the manager in last 3 months excluding business from their Category A advisor</td>
  </tr>
  <tr>
    <td>Manager_Num_Products2</td><td>	Number of products sold by the manager in last 3 months excluding business from their Category A advisor</td>
  </tr>
  <tr>
    <td> Business_Sourced(Target)	</td><td>Business sourced by applicant within 3 months [1/0] of recruitment</td>
  </tr>
 
</table>

</body>
</html>

