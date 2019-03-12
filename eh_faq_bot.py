import telebot
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from load_data import get_indv_menus, load_data, get_office_info, get_SCRC_info, get_JCRC_info, get_blockcomm_info, get_culture_info, get_sports_info, get_ss_info, get_othercomm_info, get_sponsorship_info, get_pdpa_info, get_finance_info, get_external_info, get_internal_info, get_cultural_info, get_common_info, get_others_info, get_rooms_info, get_printer_info
from load_data import get_media_equipment_info, get_ew_room_info, get_media_services_info, get_report_info, get_compulsory_info, get_graduating_info, get_cca_points_info, get_bonus_points_info, get_external_cca_info, get_exchange_info, get_monitoring_info, get_masters_list_info, get_demerit_info, get_pal_info, get_eoty_info, get_hallex_info, get_topfield_info, get_general_awards_info
import datetime as dt
import csv

token = 'TOKEN'
bot = telebot.TeleBot(token)
bf_menu, dinz_menu = load_data()

text_messages = {
    'welcome':
        u'Hello there! I am your new Eusoff FAQs & Meal Bot.\n'
        u'\nTo share: https://t.me/eusoff_bot',

    'info':
        u'Hello there!\n'
        u'I am a bot that will provide the answers to all your FAQs as well as the breakfast and dinner menus of Eusoff!\n'
        u'\nCommands\n'
        u'/start - start up the Eusoff bot\n'
        u'/info - more info about the bot and commands\n'
        u'/feedback - give us feedback on the bot (and request for features!)\n',

    'feedback':
        u'Feel free to leave down any suggestions/opinions at https://goo.gl/forms/zaOOUhiJhH8RzlZx2\n'
        u'We appreciate all kinds of feedback!'
}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, text_messages['welcome'])
    bot.send_message(message.chat.id, "Let's get started!", reply_markup=contents_markup())


@bot.message_handler(commands=['info'])
def on_info(message):
    bot.reply_to(message, text_messages['info'])


@bot.message_handler(commands=['feedback'])
def on_feedback(message):
    bot.reply_to(message, text_messages['feedback'])


def menu_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("MENU", callback_data="get_menu"))
    return markup


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Tdy's Bf 🍞", callback_data="cb_tdy_bf"),
               InlineKeyboardButton("Tdy's Dinz 🍱", callback_data="cb_tdy_din"),
               InlineKeyboardButton("Tmr's Bf 🍞", callback_data="cb_tmr_bf"),
               InlineKeyboardButton("Tmr's Dinz 🍱", callback_data="cb_tmr_din"))
    return markup

def contents_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("FAQ", callback_data="get_faq"),
               InlineKeyboardButton("Menu", callback_data="get_menu"))
    return markup

def faq_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Office", callback_data="get_halloffice"),
               InlineKeyboardButton("Committees", callback_data="get_committees"),
               InlineKeyboardButton("Sponsorship/PDPA", callback_data="get_sponsorship_markup"),
               InlineKeyboardButton("Finance Matters", callback_data="get_finance"),
               InlineKeyboardButton("Facilities booking", callback_data="get_booking"),
               InlineKeyboardButton("Media Facilities", callback_data="get_media_facilities"),
               InlineKeyboardButton("Report Faults", callback_data="get_report"),
               InlineKeyboardButton("Points System", callback_data="get_points"),
               InlineKeyboardButton("Demerit Points", callback_data="get_demerit"),
               InlineKeyboardButton("PAL Programme", callback_data="get_pal"),
               InlineKeyboardButton("The Eusoff Awards", callback_data="get_tea"),
               InlineKeyboardButton("Map of Eusoff", callback_data="get_map"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def halloffice_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Hall Office", callback_data="get_office_info"),
               InlineKeyboardButton("SCRC", callback_data="get_SCRC"),
               InlineKeyboardButton("JCRC", callback_data="get_JCRC"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def committee_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Block Comm", callback_data="get_blockcomm"),
               InlineKeyboardButton("Culture", callback_data="get_culture"),
               InlineKeyboardButton("Social Services", callback_data="get_ss"),
               InlineKeyboardButton("Sports", callback_data="get_sports"),
               InlineKeyboardButton("Others", callback_data="get_othercomm"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def sponsorship_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Sponsorship", callback_data="get_sponsorship"),
               InlineKeyboardButton("PDPA", callback_data="get_pdpa"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def finance_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def facilitytype_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("External Sports", callback_data="get_external"),
               InlineKeyboardButton("Internal Sports", callback_data="get_internal"),
               InlineKeyboardButton("Internal Cultural", callback_data="get_cultural"),
               InlineKeyboardButton("Common Facilities", callback_data="get_common"),
               InlineKeyboardButton("Other Facilities", callback_data="get_others"),
               InlineKeyboardButton("Rooms within Hall", callback_data="get_rooms"),
               InlineKeyboardButton("Printer", callback_data="get_printer"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def mediafacility_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Media Equipment", callback_data="get_media_equipment"),
               InlineKeyboardButton("EusoffWorks Room", callback_data="get_ew_room"),
               InlineKeyboardButton("Media Services", callback_data="get_media_services"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def points_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Compulsory Attendance", callback_data="get_compulsory"),
               InlineKeyboardButton("Graduating Residents", callback_data="get_graduating"),
               InlineKeyboardButton("Points System", callback_data="get_points_system"),
               InlineKeyboardButton("Things to Note", callback_data="get_things2note"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def points_notes():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("CCA Points", callback_data="get_cca_points"),
               InlineKeyboardButton("Bonus Points", callback_data="get_bonus_points"),
               InlineKeyboardButton("External CCA Points", callback_data="get_external_cca"),
               InlineKeyboardButton("Exchange", callback_data="get_exchange"),
               InlineKeyboardButton("Monitoring", callback_data="get_monitoring"),
               InlineKeyboardButton("Master's List", callback_data="get_masters_lists"),
               InlineKeyboardButton("Back", callback_data="get_points"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def demerit_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Offense Types", callback_data="get_offense_type"),
               InlineKeyboardButton("Housing Agreement", callback_data="get_housing_agreement"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

def award_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("EOTY Award", callback_data="get_eoty"),
               InlineKeyboardButton("Top Field Awards", callback_data="get_topfield"),
               InlineKeyboardButton("Hall Excellence Awards", callback_data="get_hallex"),
               InlineKeyboardButton("General Awards", callback_data="get_general_awards"),
               InlineKeyboardButton("Back", callback_data="get_faq"),
               InlineKeyboardButton("Main Page", callback_data="get_main"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    date = dt.datetime.fromtimestamp(call.message.date)
    entry = {
        'date': date,
        'button': call.data,
        'username': call.message.chat.username,
        'type': 'callbackquery'
    }
    print(call)
    if call.data == "get_main":
        bot.send_message(call.message.chat.id, 'Let\'s get started!', parse_mode='Markdown', reply_markup=contents_markup())
    if call.data == "get_menu":
        bot.send_message(call.message.chat.id, 'Select one:', parse_mode='Markdown', reply_markup=gen_markup())
    if call.data == 'get_faq':
        bot.send_message(call.message.chat.id, 'What do you wish to know?', parse_mode='Markdown', reply_markup=faq_markup())
    if call.data == "cb_tdy_bf":
        # menu=tdy_bf_m
        menu = get_indv_menus('Breakfast', date)
        bot.send_message(call.message.chat.id, menu, parse_mode='Markdown', reply_markup=menu_markup())
    if call.data == "cb_tdy_din":
        # menu=tdy_din_m
        menu = get_indv_menus('Dinner', date)
        bot.send_message(call.message.chat.id, menu, parse_mode='Markdown', reply_markup=menu_markup())
    elif call.data == "cb_tmr_bf":
        # menu=tmr_bf_m
        menu = get_indv_menus('Breakfast', date + dt.timedelta(days=1))
        bot.send_message(call.message.chat.id, menu, parse_mode='Markdown', reply_markup=menu_markup())
    elif call.data == "cb_tmr_din":
        # menu=tdy_din_m
        menu = get_indv_menus('Dinner', date + dt.timedelta(days=1))
        bot.send_message(call.message.chat.id, menu, parse_mode='Markdown', reply_markup=menu_markup())
    if call.data == "get_halloffice":
        bot.send_message(call.message.chat.id, 'Select the office information which you wish to know:', parse_mode='Markdown', reply_markup=halloffice_markup())
    if call.data == "get_office_info":
        office_info = get_office_info()
        bot.send_message(call.message.chat.id, office_info, parse_mode='Markdown', reply_markup=halloffice_markup())
    if call.data == "get_SCRC":
        SCRC_info = get_SCRC_info()
        bot.send_message(call.message.chat.id, SCRC_info, parse_mode='Markdown', reply_markup=halloffice_markup())
    if call.data == "get_JCRC":
        JCRC_info = get_JCRC_info()
        bot.send_message(call.message.chat.id, JCRC_info, parse_mode='Markdown', reply_markup=halloffice_markup())
    if call.data == "get_committees":
        bot.send_message(call.message.chat.id, 'Select Committee Type:', parse_mode='Markdown', reply_markup=committee_markup())
    if call.data == "get_blockcomm":
        block_info = get_blockcomm_info()
        bot.send_message(call.message.chat.id, block_info, parse_mode='Markdown', reply_markup=committee_markup())
    if call.data == "get_culture":
        culture_info = get_culture_info()
        bot.send_message(call.message.chat.id, culture_info, parse_mode='Markdown', reply_markup=committee_markup())
    if call.data == "get_ss":
        ss_info = get_ss_info()
        bot.send_message(call.message.chat.id, ss_info, parse_mode='Markdown', reply_markup=committee_markup())
    if call.data == "get_sports":
        sports_info = get_sports_info()
        bot.send_message(call.message.chat.id, sports_info, parse_mode='Markdown', reply_markup=committee_markup())
    if call.data == "get_othercomm":
        othercomm_info = get_othercomm_info()
        bot.send_message(call.message.chat.id, othercomm_info, parse_mode='Markdown', reply_markup=committee_markup())
    if call.data == "get_sponsorship_markup":
        bot.send_message(call.message.chat.id, 'Select One:', parse_mode='Markdown', reply_markup=sponsorship_markup())
    if call.data == "get_sponsorship":
        sponsorship_info = get_sponsorship_info()
        bot.send_message(call.message.chat.id, sponsorship_info, parse_mode='Markdown', reply_markup=sponsorship_markup())
    if call.data == "get_pdpa":
        pdpa_info = get_pdpa_info()
        bot.send_message(call.message.chat.id, pdpa_info, parse_mode='Markdown', reply_markup=sponsorship_markup())
    if call.data == "get_finance":
        finance_info = get_finance_info()
        bot.send_message(call.message.chat.id, finance_info, parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_booking":
        bot.send_message(call.message.chat.id, 'Select Facility Type:', parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_external":
        external_info = get_external_info()
        bot.send_message(call.message.chat.id, external_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_internal":
        internal_info = get_internal_info()
        bot.send_message(call.message.chat.id, internal_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_cultural":
        cultural_info = get_cultural_info()
        bot.send_message(call.message.chat.id, cultural_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_common":
        common_info = get_common_info()
        bot.send_message(call.message.chat.id, common_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_others":
       others_info = get_others_info()
       bot.send_message(call.message.chat.id, others_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_rooms":
       rooms_info = get_rooms_info()
       bot.send_message(call.message.chat.id, rooms_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_printer":
       printer_info = get_printer_info()
       bot.send_message(call.message.chat.id, printer_info, parse_mode='Markdown', reply_markup=facilitytype_markup())
    if call.data == "get_media_facilities":
       bot.send_message(call.message.chat.id, 'Select Media Facility:', parse_mode='Markdown', reply_markup=mediafacility_markup())
    if call.data == "get_media_equipment":
       media_equipment_info = get_media_equipment_info()
       bot.send_message(call.message.chat.id, media_equipment_info, parse_mode='Markdown', reply_markup=mediafacility_markup())
    if call.data == "get_ew_room":
       ew_room_info = get_ew_room_info()
       bot.send_message(call.message.chat.id, ew_room_info, parse_mode='Markdown', reply_markup=mediafacility_markup())
    if call.data == "get_media_services":
        media_services_info = get_media_services_info()
        bot.send_message(call.message.chat.id, media_services_info, parse_mode='Markdown', reply_markup=mediafacility_markup())
    if call.data == "get_report":
        report_info = get_report_info()
        bot.send_message(call.message.chat.id, report_info, parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_points":
        bot.send_message(call.message.chat.id, 'Select One:', parse_mode='Markdown', reply_markup=points_markup())
    if call.data == "get_compulsory":
        compulsory_info = get_compulsory_info()
        bot.send_message(call.message.chat.id, compulsory_info, parse_mode='Markdown', reply_markup=points_markup())
    if call.data == "get_graduating":
        graduating_info = get_graduating_info()
        bot.send_message(call.message.chat.id, graduating_info, parse_mode='Markdown', reply_markup=points_markup())
    if call.data =="get_points_system":
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/CCA_points_1.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/CCA_points_2.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/CCA_points_3.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/CCA_points_4.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/CCA_points_5.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/CCA_points_6.png', 'rb'))
        bot.send_message(call.message.chat.id, "The points system is as indicated above.", parse_mode='Markdown', reply_markup=points_markup())
    if call.data =="get_things2note":
        bot.send_message(call.message.chat.id, 'Select One:', parse_mode='Markdown', reply_markup=points_notes())
    if call.data == "get_cca_points":
        cca_points_info = get_cca_points_info()
        bot.send_message(call.message.chat.id, cca_points_info, parse_mode='Markdown', reply_markup=points_notes())
    if call.data == "get_bonus_points":
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Bonus_points.png', 'rb'))
        bonus_points_info = get_bonus_points_info()
        bot.send_message(call.message.chat.id, bonus_points_info, parse_mode='Markdown', reply_markup=points_notes())
    if call.data =="get_external_cca":
        external_cca_info = get_external_cca_info()
        bot.send_message(call.message.chat.id, external_cca_info, parse_mode='Markdown', reply_markup=points_notes())
    if call.data == "get_exchange":
        exchange_info = get_exchange_info()
        bot.send_message(call.message.chat.id, exchange_info, parse_mode='Markdown', reply_markup=points_notes())
    if call.data == "get_monitoring":
        monitoring_info = get_monitoring_info()
        bot.send_message(call.message.chat.id, monitoring_info, parse_mode='Markdown', reply_markup=points_notes())
    if call.data == "get_masters_lists":
        masters_list_info = get_masters_list_info()
        bot.send_message(call.message.chat.id, masters_list_info, parse_mode='Markdown', reply_markup=points_notes())
    if call.data == "get_demerit":
        demerit_info = get_demerit_info()
        bot.send_message(call.message.chat.id, demerit_info, parse_mode='Markdown', reply_markup=demerit_markup())
    if call.data == "get_offense_type":
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Offense_1.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Offense_2.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Offense_3.png', 'rb'))
        bot.send_message(call.message.chat.id, "Offense types and their relevant demerit points are shown above", parse_mode='Markdown', reply_markup=demerit_markup())
    if call.data == "get_housing_agreement":
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Agreement_1.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Agreement_2.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Agreement_3.png', 'rb'))
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/Agreement_4.png', 'rb'))
        bot.send_message(call.message.chat.id, "The Schedule of Administrative Fees is to be read in conjunction with the Housing Agreement and Eusoff Hall’s Rules and Regulations.", parse_mode='Markdown', reply_markup=demerit_markup())
    if call.data == "get_pal":
        pal_info = get_pal_info()
        bot.send_message(call.message.chat.id, pal_info, parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_tea":
        bot.send_message(call.message.chat.id, "Select Award Type:", parse_mode='Markdown', reply_markup=award_markup())
    if call.data == "get_map":
        bot.send_photo(call.message.chat.id, photo=open('/Users/quahjingwen/Desktop/CCA_points/map.png', 'rb'))
        bot.send_message(call.message.chat.id, "The Map of Eusoff Hall is as shown above", parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_eoty":
        eoty_info = get_eoty_info()
        bot.send_message(call.message.chat.id, eoty_info, parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_topfield":
        topfield_info = get_topfield_info()
        bot.send_message(call.message.chat.id, topfield_info, parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_hallex":
        hallex_info = get_hallex_info()
        bot.send_message(call.message.chat.id, hallex_info, parse_mode='Markdown', reply_markup=finance_markup())
    if call.data == "get_general_awards":
        general_awards_info = get_general_awards_info()
        bot.send_message(call.message.chat.id, general_awards_info, parse_mode='Markdown', reply_markup=finance_markup())
    

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Hungz???", reply_markup=gen_markup())


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Sorry, I do not understand. Try /start /help /info")

bot.polling()
