
from telethon import TelegramClient, events,Button
import telethon
from telethon.tl.types import Channel, Chat, DocumentAttributeFilename
from bs4 import BeautifulSoup

api_id = "your_id"
api_hash = 'api_hash'
phone_number = 'phone_number'

client = TelegramClient('session_name', api_id, api_hash)
# Start the client and add the event handler for new messages
from telethon.tl.functions.messages import GetDialogsRequest
from tqdm import tqdm
import os  
from telethon.tl.functions.channels import GetFullChannelRequest

async def main():
    
   

    # Start the client
    await client.start(phone_number)
   
    async def trn_pdf(c_name):
      dialogs = await client.get_dialogs() #THE magic
      result = await client(GetDialogsRequest(
                offset_date=None,
                 offset_id=0,
                 offset_peer='username',
                 limit=500,
                 hash=0,
                         ))
      X=[]
      x1=0
      a={}
      cr=0
      channel = await client(GetFullChannelRequest(c_name))
      full_channel = await client(GetFullChannelRequest(c_name))
      channel = full_channel.chats[0] 
      messages = await client.get_messages(channel, limit=205)
      download_path = './Top Students/'
      os.makedirs(download_path, exist_ok=True)
      for message in tqdm(messages):
                   
                   if hasattr(message.media, 'document'):
                    for attribute in message.media.document.attributes:
                        if isinstance(attribute, telethon.tl.types.DocumentAttributeFilename):
                            if attribute.file_name.endswith('.pdf'):
                                sol={"tag":"",
                                     "patterns":[],
                                     "responses":[]}
                                sol["tag"]="y"+str(x1)
                                
                                x1=x1+1
                                pdf_name = attribute.file_name
                                o=pdf_name
                                sol["patterns"].append("can you provide me a link for"+o+"\n")
                                sol["patterns"].append("give me a link for "+o+"\n")
                                sol["patterns"].append("what is "+o+" can i get a video link \n ")
                                sol["patterns"].append("i need a video link for "+o+"\n")
                                sol["patterns"].append("I want a video link for "+o+"\n")
                                sol["patterns"].append(" link for "+o+"\n")
                                sol["patterns"].append("can i get a video link for "+o+"\n")
                               
                                print(f"Downloading PDF '{pdf_name}'")
                                x=str(message.id)
                                
                                sol["responses"].append("Yes here it is "+x+"\n")
                                # sol["responses"].append("Of course here is a link "+x+"\n")
                                # sol["responses"].append("Sure check it "+x+"\n")
                                print(f"Downloading PDF from message {message.id}")
                                X.append(sol)
                                a[str(cr)]=X
                                if(x1==50):
                                    x1=0
                                    cr=cr+1
                                    X=[]
                                try:
                                    # Download the PDF
                                    file_path = await asyncio.wait_for(message.download_media(download_path), timeout=60)
                                    if file_path:
                                        print(f"Downloaded to {file_path}")
                                    else:
                                        print(f"Failed to download PDF from message {message.id}")
                                except asyncio.TimeoutError:
                                    print(f"Timeout error downloading PDF from message {message.id}")
                                except Exception as e:
                                    print(f"Error downloading PDF from message {message.id}: {e}")
                        else:
                             print(f"No PDF found in message {message.id}")
                    else:
                         print(f"No media found in message {message.id}")
      import json
     
      
      to="u.json"
      file_path = to
      with open(file_path, "w") as file:
    # Convert the dictionary to a JSON string and write it to the file
          json.dump(a, file)
    await trn_pdf("Top Students")
    
   
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
print("tel1")