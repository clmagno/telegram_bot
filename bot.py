from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import telegram

def start(update, context):
    

    update.message.reply_text(text="Kumusta kapatid!\nSana nasa maayos na kalagayan ka.\nAng bot na ito ay may kakayahan na tulungan kang maging updated sa mga bagong tagubilin.\n\n<b>Gamitin po natin ito ng buong ingat.</b>\n\n\nI-type lamang po ang <b><i>/tagubilin</i></b> para sa mga tagubilin" ,parse_mode=telegram.ParseMode.HTML)
    
def tagubilin(update, context):
    update.message.reply_text(
    text='-<b>Mag-anyaya po tayo mga kapatid para sa kapurihan ng Diyos.</b> \n-Huwag po tayong magpabaya sa mga pagsamba.\n- Sa mga may kasama sa tahanan na kaanib sa PNK, nagsasagawa po tayo ng pagsamba tuwing sabado sa ganap na ika-10 ng umaga.\n- Sa mga nagnanais po na tumanggap ng tungkulin, ipagbigay alam niyo lamang po sa amin upang mai-endorso namin kayo sa lokal.\n- May ginagawa po tayong mga pagbabantay sa ating bahay sambahan, sana po ay mapaglaanan din natin ng panahon.\n- Mga kapatid, pagmalasakitan po natin ang paglilinis sa ating bahay sambahan.\n- Maghanda po ang lahat sa nalalapit na Sta. Cena.',parse_mode=telegram.ParseMode.HTML)
    
def main():
    
    updater = Updater('1847416664:AAFz9XInjigAZ9gHA_SlvmdbIqV3dBbFyPA')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('tagubilin',tagubilin))
    updater.start_polling()
    updater.idle()
    
print("Bot Running smoothly")
if __name__ == '__main__':
    main()
    