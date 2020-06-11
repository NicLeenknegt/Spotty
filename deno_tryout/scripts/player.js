const token = 'BQDPxfA3Jur-4RvdYessr34s6Kn3_bOqH7uwMyTZ_PFqQllQ2Fq1xqWNlMoWbBP2aRIxYmEEmFLF7KzEoR2hq3SkgTHA6dDUfrmNCr0FXUzp9lC1fpSJ9OVKNFW8zVjHOXcSrb68bhzNbL0BrQ58kAnu8S0Lzq-oiB_FgNrf0i9CZHaXZTlVkP4';

const player = new Spotify.Player({
name: 'Web Playback SDK Quick Start Player',
getOAuthToken: cb => { cb(token); }
});
console.log("Player check");
// Error handling
player.addListener('initialization_error', ({ message }) => { console.error(message); });
player.addListener('authentication_error', ({ message }) => { console.error(message); });
player.addListener('account_error', ({ message }) => { console.error(message); });
player.addListener('playback_error', ({ message }) => { console.error(message); });

// Playback status updates
player.addListener('player_state_changed', state => { console.log(state); });

// Ready
player.addListener('ready', ({ device_id }) => {
console.log('Ready with Device ID', device_id);
});

// Not Ready
player.addListener('not_ready', ({ device_id }) => {
console.log('Device ID has gone offline', device_id);
});

// Connect to the player!
player.connect();
