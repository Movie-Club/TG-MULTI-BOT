from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.

<b><u>COMMANDS</u></b>

◉ send channel last message with
  forwerd tag to get the channel id 💯

◉ /id - your tg id & info

◉ /telegraph - reply to below 5Mb media
  to get telegraph link💯

◉ /stickerid - Reply To Any Sticker to get sticker id

To Make Logo - /logo Your Name
To Make Square Logo -  /logosq Your Name

♻️ Example:
/logo Tech Masters 
/logosq Tech Masters 

🤩THANKS FOR USING ME😍
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🤖 𝐌𝐘 𝐁𝐎𝐓𝐒", callback_data="botz")
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ 𝙼𝚄𝙻𝚃𝙸 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {bot.mention}
║┣⪼👨‍💻ᴅᴇᴠ : <a href=https://t.me/helloheartbeatboss>HeartBeat</a>
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://dashboard.heroku.com>ʜᴇʀᴏᴋᴜ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 3</a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : Pyrogram v{__version__}  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/Tech_Masters2022"),
                  InlineKeyboardButton("📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/Tech_Masters")
                  ],[            
                  InlineKeyboardButton("ℹ️ 𝐇𝐄𝐋𝐏", callback_data="help"),
                  InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
                  ],[
                  InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 👨‍💻 ", callback_data="devs"),
                  InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
                  ]]
                  )
             )
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @helloheartbeatboss",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒", url="https://t.me/helloheartbeatboss"),
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUS TEST THIS COMMANDS 😉</u></b>

◉ /runs         
◉ /ikka      
◉ /dice     
◉ /arrow    
◉ /goal    
◉ /luck    
◉ /throw     
◉ /bowling  
◉ /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                 InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="🤖 This is My botz 😁",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("ℹ️ 𝐌𝐎𝐕𝐈𝐄 𝐁𝐎𝐓", url="https://t.me/GeorgeMalarobot"),
                     InlineKeyboardButton("🎵 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓", url="https://t.me/SK_MUSIC_ROBOT")
                     ],[                   
                     InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                     InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























