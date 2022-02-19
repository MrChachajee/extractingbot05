from telegram.ext import *
from telegram import Update
import os
# from urllib3 import make_headers

os.system("apt install unzip")

BOT_API = "5243536300:AAFQrJVeFQKChsh8QEbwA-pZ4k2I2gOkLAU"
def downloader(update: Update, context: CallbackContext):
  root = f"{os.getcwd()}/extracted"
  x = 0
  os.system("rm -rf extracted r.zip")
  msg = update.message.reply_text("Downloading File")
  with open("r.zip", 'wb') as f:
    context.bot.get_file(update.message.document).download(out=f)
  os.system("mkdir extracted")
  msg.edit_text("Extracting Files")
  os.system("unzip r.zip -d extracted")
  for p, s, f in os.walk(root):
    for i in f:
      x += 1
  update.message.reply_text(f"Number Of Files: {x }")
  msg.edit_text("Sending Files")
  for path, subdirs, files in os.walk(root):
    for name in files:
      with open(os.path.join(path, name), 'rb') as f:
        context.bot.sendDocument(update.message.chat_id, document=f)
        update.message.reply_text(os.path.join(path, name))
  os.system("rm -rf extracted r.zip")
updater = Updater(BOT_API, use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))

updater.start_polling()
updater.idle()