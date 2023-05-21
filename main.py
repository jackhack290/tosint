#!/usr/bin/env python3
import telegram


def main():
    telegram_token = input("6212262263:AAFATY83PYIqroPxGb2gIJVfdOLowtVAuAs): ").strip()
    telegram_chat_id = input("Telegram Chat ID (-100xxx): ").strip()

    if telegram_token.startswith("bot"):
        telegram_token = telegram_token[3:]

    print("\nAnalysis of token: " + str(telegram_token) + " and chat id: " + str(telegram_chat_id) + "\n")

    try:
        bot = telegram.Bot(telegram_token)
    except Exception as e:
        print("Error: " + str(e))
        bot = None
        exit()

    if bot:
        try:
            telegram_get_me = bot.getMe()
            print("Bot First Name: " + str(telegram_get_me["first_name"]))
            print("Bot Username: " + str(telegram_get_me["username"]))
            telegram_bot_user_id = telegram_get_me["id"]
            print("Bot User ID: " + str(telegram_bot_user_id))
            print("Bot Can Read Group Messages: " + str(telegram_get_me["can_read_all_group_messages"]))
            telegram_get_chat_member = bot.get_chat_member(telegram_chat_id, telegram_bot_user_id)
            print("Bot In The Chat Is An: " + telegram_get_chat_member["status"])
        except:
            pass

        try:
            telegram_get_chat = bot.getChat(telegram_chat_id)
            print("Chat Title: " + str(telegram_get_chat["title"]))
            print("Chat Type: " + str(telegram_get_chat["type"]))
            print("Chat ID: " + str(telegram_get_chat["id"]))
            print("Chat Username: " + str(telegram_get_chat["username"]))
            print("Chat Invite Link: " + str(telegram_get_chat["invite_link"]))
        except:
            pass

        try:
            telegram_chat_invite_link = bot.export_chat_invite_link(telegram_chat_id)
            print("Chat Invite Link: " + str(telegram_chat_invite_link))
        except:
            pass

        try:
            telegram_chat_invite_link = bot.create_chat_invite_link(telegram_chat_id)
            print("Create Invite Link: " + str(telegram_chat_invite_link["invite_link"]))
        except:
            pass

        try:
            telegram_get_updates = bot.getUpdates(telegram_chat_id)
            if telegram_get_updates:
                print("Updates:")
                for update in telegram_get_updates:
                    print(update["channel_post"])
        except:
            pass

        try:
            telegram_chat_members_count = bot.get_chat_member_count(telegram_chat_id)
            print("Number of users in the chat: " + str(telegram_chat_members_count))
        except:
            pass

        try:
            telegram_get_chat_administrators = bot.get_chat_administrators(telegram_chat_id)
            if telegram_get_chat_administrators:
                print("Administrators in the chat:")
                for user in telegram_get_chat_administrators:
                    print(user["user"])
        except:
            pass


if __name__ == "__main__":
    main()
