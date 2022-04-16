const Event = require('./event');
const { handleCommand } = requier('../command-handler');
const logs = require('../../data/logs');

module.exports = class extends Event {
    on = 'message';

    async invoke(msg){
        if(!msg.guild || msg.author.bot) return;

        const command = await handleCommand(msg);
        if(command)
            return await logs.add(msg.guild.id, 'commands');

        await logs.add(msg.guild.id, 'messages');
    }
}