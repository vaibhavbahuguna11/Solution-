#!/usr/bin/env python
# coding: utf-8

# # CREATION OF DATA STRUCTURE

# In[20]:


team_details={
   'GT':['GT',20,['W','W','L','L','W']]
    
   ,'LSG':['LSG',18,['W','L','L','W','W']]
    
   ,'RR':['RR',16,['W','L','W','L','L']]
    
    ,'DC':['DC',14,['W','W','L','W','L']]
    
    ,'RCB':['RCB',14,['L','W','W','L','L']]
    
    ,'KKR':['KKR',12,['L','W','W','L','W']]
    
    ,'PBKS':['PBKS',12,['L','W','L','W','L']]
    
    ,'SRH':['SRH',12,['W','L','L','L','L']]
    
    ,'CSK':['CSK',8,['L','L','W','L','W']]
    
    ,'MI':['MI',6,['L','W','L','W','W']]
}


# # Programmatically retrieve the teams that have 2 consecutive losses.

# In[21]:


# create a function that returns a team having two consecutive losses

def retrive_team_two_losses(team): 
#     iterating using for_loop for reading two consecutive losses
    for result in range(len(team[-1])-1):  
        if team[-1][result]==team[-1][result+1] and team[-1][result]=='L':    
            return team[0]
            
        


# In[22]:


# iterating using for loop to get all the teams having two consecutive losses

for team in team_details.keys():
    get_team=retrive_team_two_losses(team_details[team])
    if get_team is not None:
        print(get_team)


# # Generalizing the solution, so that we could get teams that have n consecutive losses/wins.
# 

# In[29]:


# create a function that returns a team having n consecutive losses or wins
def retrive_team_n_losses_or_wins(team,n):
    for i in range(len(team[-1])-n+1):
        if (team[-1][i:i+n]==['W']*n) or (team[-1][i:i+n]==['L']*n) :
            return team[0]  
        


# In[30]:


# getting the values og n
Y=True
while Y:
    n=int(input('enter the valid  value of consecutive losses or wins: '))
    if n>5:
        continue
    else:
        Y=False


# In[32]:


# iterating using for loop to get all the teams having n consecutive losses or wins
filtered_teams=[]
for team in team_details.keys():
    x=retrive_team_n_losses_or_wins(team_details[team],n)
    if x is not None:
        filtered_teams.append(x)
        print(x)    


# In[33]:


print(filtered_teams)


# #  Average of points of these filtered teams
# 

# In[34]:


sum_of_points=0
for team in filtered_teams:
    sum_of_points+=team_details[team][1]
average_of_points=sum_of_points/len(filtered_teams)
print(average_of_points)
    


# In[ ]:




