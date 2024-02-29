from TikTokLive.client.client import TikTokLiveClient
from TikTokLive.client.logger import LogLevel
from TikTokLive.events import GiftEvent
from TikTokLive.events import ConnectEvent, CommentEvent


client: TikTokLiveClient = TikTokLiveClient(
    unique_id="@uwu_akyla"
)


@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    client.logger.info(f"Connected to @{event.unique_id}!")


@client.on(GiftEvent)
async def on_comment(event: GiftEvent):
    '''gifts from users'''
    client.logger.info("Received a gift!")

    try:
        if event.gift.streakable and not event.streaking:
            print('''┈┈┈☆☆☆☆☆☆☆┈┈┈
            ┈┈╭┻┻┻┻┻┻┻┻┻╮┈┈
            ┈┈┃╱╲╱╲╱╲╱╲╱┃┈┈
            ┈╭┻━━━━━━━━━┻╮┈
            ┈┃╱╲╱╲╱╲╱╲╱╲╱┃┈
            ┈┗━━━━━━━━━━━┛┈ ''')
            print(f"\n{event.user.unique_id} отправил подарок \"{event.gift.name}\"\n\n________________\n")

        # Cannot have a streak
        elif not event.gift.streakable:
            print('''┈┈┈☆☆☆☆☆☆☆┈┈┈
            ┈┈╭┻┻┻┻┻┻┻┻┻╮┈┈
            ┈┈┃╱╲╱╲╱╲╱╲╱┃┈┈
            ┈╭┻━━━━━━━━━┻╮┈
            ┈┃╱╲╱╲╱╲╱╲╱╲╱┃┈
            ┈┗━━━━━━━━━━━┛┈ ''')
            print(f"\n{event.user.unique_id} отправил подарок \"{event.gift.info.name}\"\n\n________________\n")
    except:
        print()


async def on_comment2(event: CommentEvent):
    '''comments from users'''
    try:
        print(f"| {event.user.nickname} |       ->      {event.comment}")
    except:
        print()


client.add_listener(CommentEvent, on_comment2)

if __name__ == '__main__':
    # Enable debug info
    client.logger.setLevel(LogLevel.INFO.value)

    # Connect
    client.run()
