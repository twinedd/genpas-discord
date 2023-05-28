@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('genpas'):
        await message.channel.send(gen_pass(10))

    if message.content.startswith('random'):
        if random.randint(1,2) == 1:
            await message.channel.send('решка')
        else:
            await message.channel.send('орел')
