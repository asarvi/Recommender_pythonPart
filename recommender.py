from collections import Counter
import random
#a counter for list
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

#function for search in list
def listContains(list , object):
    j =0
    for i in list:
        if object==i:
            j=1
    if j>0:
        return 1
    elif j==0:
        return 0


#function e farzi baraye be dast avardane aspect
def aspectDetector(rev):
    revi = rev.split()
    aspec =[]
    #felan farz mikonim token 3 va 5 aspect hastan
    x = len(revi)
    if(x>5):
         aspec.append(revi[5])
         aspec.append(rev[3])

    return aspec


# function e farzi baraye be dast avardane + ya - aspect
def aspectSentiment(comment ,aspec):
    #felan random khuruji mide
    sent =random.choice([0,1,2])
    return  sent


def recommend(productname , negativeAspect):
    productFile = open('RecommendedObjects' + productname+ '.txt')
    #dictionary to keep the repeatation of products in files
    dic = {}

    listOfProducts = []

    #final recommended objects:

    recomList= []

    for p in productFile:
        temp = p.split('	')
        tempProduct = temp[0]
        listOfProducts.append(tempProduct)

    #print(listOfProducts)


    #count each product
    for l in listOfProducts:
        count =countX(listOfProducts , l)
        dic[l] = count

    #print(len(dic))


    #now look for each item
    counter = 0

    productFile = open('RecommendedObjects' + productname + '.txt')
    for n in (dic):

        for m,line in enumerate(productFile):
            if counter <= m < counter + dic.get(n):

                comment = ""
                counter = counter+1
                temp = line.split('	')
                productID = temp[0]
                # split comments from product id
                for j in range(1, len(temp)):
                    comment = comment + temp[j] + " "
                aspects =aspectDetector(comment)
                if (listContains(aspects , negativeAspect)):

                    #if  aspect was +
                    if (aspectSentiment(comment ,negativeAspect)< 2):
                        recomList.append(productID)

                        recomList = list(dict.fromkeys(recomList))

                    elif (aspectSentiment(comment ,negativeAspect)==2):
                        if(listContains(recomList,productID)):
                          recomList.remove(productID)
                          recomList = list(dict.fromkeys(recomList))


                elif(listContains(aspects , negativeAspect))<1:
                    #print(productID)
                    recomList.append(productID)
                    recomList = list(dict.fromkeys(recomList))


    #hazfe tekraria az list

    print(recomList)
    return recomList



#open testfile
testFile = open('TestFile.txt', 'r')

#array definition
reviewPart =[]
# recall

#read line by line
for line in testFile:
    reviewPart= line.split('%%&%%')

    trueRecommendation = 0
    falseRecommendarion = 0

   # print(reviewPart[1])
    review = reviewPart[1]

    #temp is the array which splits review
    temp = review.split(' ')

    #negative aspect of product
    negativeAspect = temp[1]

    recommends = reviewPart[0].split('    ')[1]
    recommendObjects = recommends.split();
    product = reviewPart[0].split('    ')[0]
    recomlist =recommend(product , negativeAspect)

    for obj in recomlist:

         if (listContains(recommendObjects,obj)):
             trueRecommendation = trueRecommendation+1
         else:
            falseRecommendarion = falseRecommendarion+1
  #  print("recall for product " + product)
    print((trueRecommendation)/(len(recomlist)))










