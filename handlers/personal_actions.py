from aiogram import types
from dispatcher import dp
from aiogram.dispatcher.filters import Text
import config
import random
from array import *

BOT_OWNER = 1372293047

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import re
from bot import BotDB

@dp.message_handler(commands = ["kob"])
async def kob_command(message: types.Message):
    value = message.text
    arr = value.split()
    value = value.replace(arr[0], '').strip()
    value = value.replace(arr[1], '').strip()
    arr.pop(0)
    await message.bot.send_message(int(arr[0]), value)
    await message.bot.send_message(BOT_OWNER, "command from @" + str(message.from_user.username) + ' to ' + str(arr[0]) + ' ' + str(value))
   
@dp.message_handler(commands = ("history", "h"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = ('/history', '/h', '!history', '!h')
    within_als = {
        "day": ('today', 'day', 'сегодня', 'день'),
        "month": ('month', 'месяц'),
        "year": ('year', 'год'),
    }

    cmd = message.text
    for r in cmd_variants:
        cmd = cmd.replace(r, '').strip()

    within = 'day'
    if(len(cmd)):
        for k in within_als:
            for als in within_als[k]:
                if(als == cmd):
                    within = k

    records = BotDB.get_records(message.from_user.id, within)

    if(len(records)):
        answer = f"🕘 История операций за {within_als[within][-1]}\n\n"

        for r in records:
            answer += "<b>" + ("➖ Расход" if not r[2] else "➕ Доход") + "</b>"
            answer += f" - {r[3]}"
            answer += f" <i>({r[4]})</i>\n"

        await message.reply(answer)
    else:
        await message.reply("Записей не обнаружено!")











@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
    button_random_cat = KeyboardButton('🐱🐱🐱')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    #greet_kb.add(button_invite, button_random_cat)
    greet_kb.add(button_random_cat)
    await message.answer('Hey',reply_markup=greet_kb)

@dp.message_handler(lambda message: message.text == "494444")
async def process_randcat(message: types.Message):
    await message.answer("https://t.me/+ygdHL1GTWZllMTYy")

# secret page
@dp.message_handler(lambda message: message.text == "079450327")
async def process_secret(message: types.Message):
    await message.answer('плюмпики катики леники хорошики мявики семейки... u_u')

@dp.message_handler(Text(contains='кот', ignore_case=True))
@dp.message_handler(Text(contains='плюш', ignore_case=True))
@dp.message_handler(Text(contains='плюп', ignore_case=True))
@dp.message_handler(Text(contains='мяв', ignore_case=True))
@dp.message_handler(Text(contains='кош', ignore_case=True))
@dp.message_handler(Text(contains='cat', ignore_case=True))
@dp.message_handler(Text(contains='kitty', ignore_case=True))
async def process_randcat_ero(message: types.Message):
    cats = [
        'CAACAgIAAxkBAAEEYgRiTKPmQH2TqmM0AlfB3lxBD8GrbgACLhcAAnbsqUhSONZmcbrzYSME',
        'CAACAgIAAxkBAAEEYgZiTKP18IIy7FOK7zA814u87sHgUQACKxYAAlL-QUkTlcssdcKwByME',
        'CAACAgIAAxkBAAEEYghiTKQMdOMLAuOjLG7AriQbH67I8AACIhMAAjGVQUnDun6DQKPWQSME',
        'CAACAgIAAxkBAAEEYgpiTKQbnBTk1UY7qFMYfe4oujUafQACeBcAAl5e6Uua4FtQMS7rZiME',
        'CAACAgIAAxkBAAEEYiJiTKUgvRQKchCvU1AcU37WDtAExQACcBIAAo1uGUhRUkL5gjt1WCME',
        'CAACAgIAAxkBAAEEYg5iTKQ1mRwBrD8NSXDESG9ANWrQ7gAC4RcAAjJ2KEhk_AG4J7o5iSME',
        'CAACAgIAAxkBAAEEYiZiTKVTTfGyMNbx1HEBOyGE4tpKPwAC1RYAAnLeMUj1r--RPMdj-yME',
        'CAACAgIAAxkBAAEEYhJiTKRGwaoxEDTTymbs4yLlRA-RngACDBkAAiZiyUtfSS1RShAQXCME',
        'CAACAgIAAxkBAAEEYhRiTKRNRjgIDyX458GLDcOeXmjgFAAC6BQAAmrfyUuCW-2PIL3BMSME',
        'CAACAgIAAxkBAAEEYhZiTKRWadU3pXfDuU1CZjzI93IWTwACnRMAAo3R0UtBlgtVJTVjbCME',
        'CAACAgIAAxkBAAEEYhhiTKRe0brNvzcdhCvwAAEHUpUm18UAAjcUAALP48lL-1cPeXwzvDQjBA',
        'CAACAgIAAxkBAAEEYhpiTKSaefd-Bb4wpK5w4zRRzL-daQAC1xUAAjni0Euew4kBM4ZPZCME',
        'CAACAgIAAxkBAAEEYhxiTKSimOPsp7p3iQEJD0YYTmHGhgAChhoAAq2BwUtEuouDJcO3XyME',
        'CAACAgIAAxkBAAEEYh5iTKSw5MBJPB5Ph5OpP2RI7vV6PwACixQAAtMncEjDbeKmKcIRGCME',
        'CAACAgIAAxkBAAEEYi5iTKq9CRnVCBpsFNGpY8SpPCOiwAACMxUAAhZmSEkuOG9iyhH7RSME',
        'CAACAgIAAxkBAAEEYjBiTKrSt7y5PvuqUHbQyMFiuMgxFgAC9BUAAmAPKEjThgapEZbujCME',
        'CAACAgIAAxkBAAEEYkZiTKv8rr6zQqbgOVcuQ6mkEtSazwACxRcAAkHhKEgeEKdULvTz5yME',
        'CAACAgIAAxkBAAEEYjRiTKtAWDAmF0qmb6IT0XdOEaPxqAAC0Q8AAqeAyEtx1lPcgJ-pWSME',
        'CAACAgIAAxkBAAEEYjViTKtBj0PUbErAmQlj1VgRDxrmqgACChoAAojy0EtnWpcq_Ye04SME',
        'CAACAgIAAxkBAAEEYjhiTKtS0O5HkzliYfqujynZCtjlBwACqRYAAqnQ0UtEsMKQ0Z3RbyME',
        'CAACAgIAAxkBAAEEYjpiTKtYcpEwD8SEsslWszSf59_zNgACpBIAAopt8EuzZOCk0OgHQSME',
        'CAACAgIAAxkBAAEEYjxiTKt2hLBBJiUUm9dlwsuWFegIFwACdhcAAtUsaUh8hC0Y9ciSbyME',
        'CAACAgIAAxkBAAEEYj5iTKt_yOM7HeXRwZUjVIBGuP8sjgACjhcAAgzYaUjbXjCV4aGCOyME',
        'CAACAgIAAxkBAAEEYkJiTKuuyLA_bXE1xoVc_msY1x1xjAAC3hYAAkAi6Ut6vdE_cd-0-yME'
    ] 
    await message.bot.send_message(BOT_OWNER, '<b>' + '@' + str(message.from_user.username) + ' запустил котика.</b>\n', parse_mode='HTML')
        
    rare_cats = [
        'CAACAgIAAxkBAAEEbgFiUr9q-33L1vL03GnrBLDwNt4K0gACURcAAlruoEi4bgxZ-6AvDiME',
        'CAACAgIAAxkBAAEEbhNiUsXBldYU4W9VrfSXdrupNhfS5AACURUAAu_8QEtiMsBImzZF_CME',
        'CAACAgIAAxkBAAEEbhRiUsXB8v-eKG2x1iFIX37bV26ebgACQhMAAopDQUtXbbLsKW00RSME',
        'CAACAgIAAxkBAAEEbhViUsXBnCmHsAfosSvdX0WXlvqliQACeBQAAokOQUvMGMzwzDHFyCME'
    ]

    if (random.randint(0, 100) == 1):
        await message.answer_sticker(rare_cats[random.randint(0,len(rare_cats) - 1)])
        await message.answer('Вы выбили редкого котика!')
        await message.answer_sticker('CAACAgIAAxkBAAEEbhliUsbGl5gAAVQh9hGjJtVWaW7VYxkAApMRAAI__MhLCCfk7ZTOAU4jBA')
    else: 
        await message.answer_sticker(cats[random.randint(0,len(cats) - 1)])
    


@dp.message_handler(lambda message: message.text == '🐱🐱🐱')
async def process_randcat(message: types.Message):
    cats = [
        'CAACAgIAAxkBAAEEYgRiTKPmQH2TqmM0AlfB3lxBD8GrbgACLhcAAnbsqUhSONZmcbrzYSME',
        'CAACAgIAAxkBAAEEYgZiTKP18IIy7FOK7zA814u87sHgUQACKxYAAlL-QUkTlcssdcKwByME',
        'CAACAgIAAxkBAAEEYghiTKQMdOMLAuOjLG7AriQbH67I8AACIhMAAjGVQUnDun6DQKPWQSME',
        'CAACAgIAAxkBAAEEYgpiTKQbnBTk1UY7qFMYfe4oujUafQACeBcAAl5e6Uua4FtQMS7rZiME',
        'CAACAgIAAxkBAAEEYiJiTKUgvRQKchCvU1AcU37WDtAExQACcBIAAo1uGUhRUkL5gjt1WCME',
        'CAACAgIAAxkBAAEEYg5iTKQ1mRwBrD8NSXDESG9ANWrQ7gAC4RcAAjJ2KEhk_AG4J7o5iSME',
        'CAACAgIAAxkBAAEEYiZiTKVTTfGyMNbx1HEBOyGE4tpKPwAC1RYAAnLeMUj1r--RPMdj-yME',
        'CAACAgIAAxkBAAEEYhJiTKRGwaoxEDTTymbs4yLlRA-RngACDBkAAiZiyUtfSS1RShAQXCME',
        'CAACAgIAAxkBAAEEYhRiTKRNRjgIDyX458GLDcOeXmjgFAAC6BQAAmrfyUuCW-2PIL3BMSME',
        'CAACAgIAAxkBAAEEYhZiTKRWadU3pXfDuU1CZjzI93IWTwACnRMAAo3R0UtBlgtVJTVjbCME',
        'CAACAgIAAxkBAAEEYhhiTKRe0brNvzcdhCvwAAEHUpUm18UAAjcUAALP48lL-1cPeXwzvDQjBA',
        'CAACAgIAAxkBAAEEYhpiTKSaefd-Bb4wpK5w4zRRzL-daQAC1xUAAjni0Euew4kBM4ZPZCME',
        'CAACAgIAAxkBAAEEYhxiTKSimOPsp7p3iQEJD0YYTmHGhgAChhoAAq2BwUtEuouDJcO3XyME',
        'CAACAgIAAxkBAAEEYh5iTKSw5MBJPB5Ph5OpP2RI7vV6PwACixQAAtMncEjDbeKmKcIRGCME',
        'CAACAgIAAxkBAAEEYi5iTKq9CRnVCBpsFNGpY8SpPCOiwAACMxUAAhZmSEkuOG9iyhH7RSME',
        'CAACAgIAAxkBAAEEYjBiTKrSt7y5PvuqUHbQyMFiuMgxFgAC9BUAAmAPKEjThgapEZbujCME',
        'CAACAgIAAxkBAAEEYkZiTKv8rr6zQqbgOVcuQ6mkEtSazwACxRcAAkHhKEgeEKdULvTz5yME',
        'CAACAgIAAxkBAAEEYjRiTKtAWDAmF0qmb6IT0XdOEaPxqAAC0Q8AAqeAyEtx1lPcgJ-pWSME',
        'CAACAgIAAxkBAAEEYjViTKtBj0PUbErAmQlj1VgRDxrmqgACChoAAojy0EtnWpcq_Ye04SME',
        'CAACAgIAAxkBAAEEYjhiTKtS0O5HkzliYfqujynZCtjlBwACqRYAAqnQ0UtEsMKQ0Z3RbyME',
        'CAACAgIAAxkBAAEEYjpiTKtYcpEwD8SEsslWszSf59_zNgACpBIAAopt8EuzZOCk0OgHQSME',
        'CAACAgIAAxkBAAEEYjxiTKt2hLBBJiUUm9dlwsuWFegIFwACdhcAAtUsaUh8hC0Y9ciSbyME',
        'CAACAgIAAxkBAAEEYj5iTKt_yOM7HeXRwZUjVIBGuP8sjgACjhcAAgzYaUjbXjCV4aGCOyME',
        'CAACAgIAAxkBAAEEYkJiTKuuyLA_bXE1xoVc_msY1x1xjAAC3hYAAkAi6Ut6vdE_cd-0-yME'
    ]
    button_random_cat = KeyboardButton('🐱🐱🐱')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    #greet_kb.add(button_invite, button_random_cat)
    greet_kb.add(button_random_cat)
    await message.bot.send_message(BOT_OWNER, '<b>' + '@' + str(message.from_user.username) + ' запустил котика.</b>\n', parse_mode='HTML')
        
    rare_cats = [
        'CAACAgIAAxkBAAEEbgFiUr9q-33L1vL03GnrBLDwNt4K0gACURcAAlruoEi4bgxZ-6AvDiME',
        'CAACAgIAAxkBAAEEbhNiUsXBldYU4W9VrfSXdrupNhfS5AACURUAAu_8QEtiMsBImzZF_CME',
        'CAACAgIAAxkBAAEEbhRiUsXB8v-eKG2x1iFIX37bV26ebgACQhMAAopDQUtXbbLsKW00RSME',
        'CAACAgIAAxkBAAEEbhViUsXBnCmHsAfosSvdX0WXlvqliQACeBQAAokOQUvMGMzwzDHFyCME'
    ]

    if (random.randint(0, 100) == 1):
        await message.answer_sticker(rare_cats[random.randint(0,len(rare_cats) - 1)])
        await message.answer('Вы выбили редкого котика!')
        await message.answer_sticker('CAACAgIAAxkBAAEEbhliUsbGl5gAAVQh9hGjJtVWaW7VYxkAApMRAAI__MhLCCfk7ZTOAU4jBA', reply_markup=greet_kb)
    else: 
        await message.answer_sticker(cats[random.randint(0,len(cats) - 1)], reply_markup=greet_kb)
    
    await message.bot.delete_message(message.from_user.id, message.message_id)

### CALLBACK

@dp.message_handler(content_types=types.ContentType.ANY)
async def process_all(message: types.Message):
    if message.text is not None:
        await message.bot.send_message(BOT_OWNER, '<b>' + 'from: ' + '@' + str(message.from_user.username) + '\n' + 'text: ' + '</b>' + str(message.text), parse_mode='HTML')
    elif message.photo is not None:
        await message.bot.send_message(BOT_OWNER, '<b>' + 'from: ' + '@' + str(message.from_user.username) + '</b>', parse_mode='HTML')
        await message.bot.send_photo(BOT_OWNER, photo=message.photo[-1].file_id,
                             caption=str(message.caption))
    elif message.sticker is not None:
        await message.bot.send_message(BOT_OWNER, '<b>' + 'from: ' + '@' + str(message.from_user.username)  + '</b>', parse_mode='HTML')
        await sendSticker(BOT_OWNER, message.sticker.file_id)
    else:
        await message.bot.send_message(BOT_OWNER, '<b>' + 'somethig by: ' + '@' + str(message.from_user.username)+ '</b>', parse_mode='HTML')
