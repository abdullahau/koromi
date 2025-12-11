import reflex as rx

config = rx.Config(
    app_name="koromi",
    frontend_port=3001,
    backend_port=3003,
    backend_host="100.125.140.11",
    api_url="http://100.125.140.11:3003",
    deploy_url="http://100.125.140.11:3001",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
