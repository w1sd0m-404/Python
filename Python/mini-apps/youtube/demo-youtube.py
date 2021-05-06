import pandas as pd

df = pd.read_csv("USvideos.csv")

#İlk 10 kaydı getirin

#print(df.head(10))

#İkinci 5 kaydı getirin

#print(df[10:15].head(5))

#Dataset te bulunan kolon isimlerini ve sayılarını bulun

#print(df.columns)
#print(len(df.columns))

#Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyin
#(tumbnail_link,comments_disabled,ratings_disabled,)

#result = df.drop(columns=["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)
#print(result)

#Like ve dislike ortalamalarını alın

#result = df[["likes","dislikes"]].mean()
#print(result)

#İlk 50 videonun like ve dislike bölümlerini getirin

#result = df[["likes","dislikes"]].head(50)
#print(result)

#En çok görüntülenen video hangisidir

#result = df[df["views"]==df["views"].max()]["title"].iloc[0]
#print(result)

#En düşük görüntülenen video hangisidir

#result = df[df["views"]==df["views"].min()]["title"].iloc[0]
#print(result)

#En fazla görüntülenen ilk 10 video

#result = df.sort_values("views",ascending=False).head(10)[["title","views"]]
#print(result)

#Kategoriye göre beğeni ort sıralı bir şekilde getirin

#result = df.groupby("category_id").mean().sort_values("likes")["likes"]
#print(result)

#Kategoriye göre yorum sayılarını yukarıdan aşağı sıralayınız

#result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]
#print(result)

#Her kategoride kaç video vardır

#result = df["category_id"].value_counts()
#print(result)

#Her videonun title uzunluğunu yeni bir kolonda gösteriniz

#df["title_len"] = df["title"].apply(len)
#result = df
#print(result)

#Her video için kullanılan tag sayısını yeni bir kolonda gösteriniz

#df["tag_len"] = df["tags"].apply(lambda x: len(x.split("|")))
#result = df
#print(result)

#En popüler videoları listeleyiniz(like,dislike oranlarına göre)

def ortHesaplama(dataset):
    likeList = list(dataset["likes"])
    dislikeList = list(dataset["dislikes"])

    liste = list(zip(likeList,dislikeList)) # tuple oluşturur. (1224like,232dislike) şeklinde

    oranListesi = []

    for like,dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi


df["begeni_orani"]= ortHesaplama(df)

print(df.sort_values("begeni_orani",ascending=False)[["likes","dislikes","begeni_orani"]])