import tweepy
import typing
import get_auth

list_name = "follow osashimi"

def find_members(api: tweepy.API, listID: str)->typing.Set[int]:
  return set([x.id for x in tweepy.Cursor(api.list_members, list_id=listID).items()])

def find_friends(api: tweepy.API)->typing.Set[int]:
  return set(list(tweepy.Cursor(api.friends_ids, user_id=api.me().id).items()))

def create_list(api: tweepy.API)->int:
  return api.create_list(name=list_name, mode="private").id

# リストを探しIDを返す、なければ新しく作る
def find_list(api: tweepy.API)->int:
  for l in api.lists_all():
    if l.name == list_name:
      return l.id
  print("リスト作成")
  return create_list(api)

def sync_list(api: tweepy.API, list_id: int, friends: typing.Set[int], members: typing.Set[int]):
  friends2 = friends | {api.me().id}

  # リストに追加
  for id in friends2-members:
    print("リスト追加: " + str(id))
    api.add_list_member(list_id=list_id, user_id=id)
  # リストから削除
  for id in members-friends2:
    print("リスト削除: " + str(id))
    api.remove_list_member(list_id=list_id, user_id=id)

def sync(api: tweepy.API, list_id: int):
  try:
    members = find_members(api, list_id)
    friends = find_friends(api)

    sync_list(api, list_id, friends, members)

  except tweepy.TweepError as e:
    print(e.reason)