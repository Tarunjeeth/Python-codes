no=(1,2,43,54,323,53,42,87,84,86)
oddsum=0
evensum=0
oddplacesum=0
evenplacesum=0
for i in range(len(no)):
    if(no[i]%2==0):
        evensum=evensum+no[i]
    else:
        oddsum=oddsum+no[i]
    if((i+1)%2==0):
        evenplacesum=evenplacesum+no[i]
    else:
        oddplacesum=oddplacesum+no[i]

print("evensum",evensum)
print("oddsum",oddsum)
print("evenplacesum",evenplacesum)
print("oddplacesum",oddplacesum)
    
