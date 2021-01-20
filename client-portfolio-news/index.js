(async function (window) {
    const applicationDefinitions = [
        {
            "title": "Clients",
            "type": "window",
            "name": "clients",
            "hidden": false,
            "details": {
                "url": "http://127.0.0.1:5000/clients/",
                "top": 25,
                "left": 800,
                "height": 400,
                "width": 400,
                "allowChannels": true
            }
        },
        {
            "title": "Portfolio",
            "type": "window",
            "name": "portfolio",
            "hidden": false,
            "details": {
                "url": "http://127.0.0.1:5000/stocks/",
                "top": 25,
                "left": 800,
                "height": 400,
                "width": 400,
                "allowChannels": true
            }
        },
        {
            "title": "News",
            "type": "window",
            "name": "news",
            "hidden": false,
            "details": {
                "url": "http://127.0.0.1:5000/news/",
                "top": 25,
                "left": 800,
                "height": 400,
                "width": 400
            }
        }
    ];

    const channelDefinitions = [
        {
            "name": "Red",
            "meta": {
                "color": "red"
            },
            "data": {
                "clientId": "VVDvc6i99J",
                "clientName": "Vernon Mullen"
            }
        },
        {
            "name": "Green",
            "meta": {
                "color": "green"
            },
            "data": {
                "clientId": "SGvc6a87J",
                "clientName": "Sutton Edwards"
            }
        },
        {
            "name": "Blue",
            "meta": {
                "color": "#66ABFF"
            },
            "data": {
                "clientId": "xZvXP2i93P",
                "clientName": "Alan Muller"
            }
        }
    ];

    // Glue42 Web Platform initialization configuration object.
    const config = {
        applications: {
            local: applicationDefinitions
        },
        channels: {
            definitions: channelDefinitions
        }
    };

    // Entry point.
    await window.createMainApp(config);

    window.displayApplicationsList(applicationDefinitions);
})(window || {});