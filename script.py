'''
Pseudocode
- take in the two lists of the users 
- read each txt file into a list
- check from the following list if it is in the followers list 
- if not, then add that to another list 
'''

# Prompt user to enter the file path
followingFile = input("Please enter the path to your text file that contains your list of following: ")


# Open and read the file
try:
    with open(followingFile, 'r', encoding ='utf-8') as file: #'r' means read mode
        content = file.read()
        print("File content read successfully")
        ###print(content)
except FileNotFoundError:
    print("The file was not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

followingList= []
# gets all the following into list
with open(followingFile, 'r', encoding='utf-8') as file:
    for username in file:
        followingList.append(username.strip())

#print (followingList)

# now get the other file
followersFile = input("Please enter the path to your text file that contains your list of followers: ")

try:
    with open(followersFile, 'r', encoding ='utf-8') as file: #'r' means read mode
        content = file.read()
        print("File content read successfully")
        ###print(content)
except FileNotFoundError:
    print("The file was not found. Please check the path.")
except Exception as e:
    print(f"An error occurred: {e}")

followersList= []
# gets all the followers into list
with open(followersFile, 'r', encoding='utf-8') as file:
    for username in file:
        followersList.append(username.strip())

#print (followersList)

#veiny ahh dih long ahh dih
# blah blah 
'''
# to push something use these commands 
git add . 
git commit -m "message you wanna put"
git push origin master

# to add to another branch
git checkout
git branch <enter branch name>
git branch model
git add .
git push origin main 
if collaborating it will make u pull his code first and then you can push yours you want

'''

auraMoggers=[]
moggercount=0
# now check following who are not in followers list, (following - followers)
for following in followingList:
    if following not in followersList:
        auraMoggers.append(following)
        moggercount+=1

for mogger in auraMoggers:
    print (mogger)
print(f"{moggercount} instagram users are currently aura mogging you on instagram")



