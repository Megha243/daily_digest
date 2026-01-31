from src.services.db import init_db, save_items, get_items, clear_items
from src.tools.fetch_hn import fetch_hacker_news
from src.tools.fetch_product import fetch_product_news
from src.services.llm_client import query_llm
from src.services.delivery import send_email, send_telegram
import asyncio

def format_section_html(heading, items, summaries):
    section = f"<h2>{heading}</h2>\n"
    for item, summary in zip(items, summaries):
        section += f"<h3><a href='{item['link']}'>{item['title']}</a></h3>\n"
        section += f"<p>{summary}</p>\n"
    return section

def format_section_html_telegram(heading, items, summaries):
    section = f"<b>{heading}</b>\n\n"
    for item, summary in zip(items, summaries):
        section += f"<b><a href=\"{item['link']}\">{item['title']}</a></b>\n"
        section += f"{summary}\n\n"
    return section

def format_section_markdown(heading, items, summaries):
    section = f"## {heading}\n\n"
    for item, summary in zip(items, summaries):
        section += f"### [{item['title']}]({item['link']})\n\n"
        section += f"{summary}\n\n"
    return section

def main():
    # --- Database Setup ---
    init_db()
    clear_items()

    # --- Fetch & Save AI & Tech News ---
    tech_items = fetch_hacker_news()
    save_items(tech_items)

    # --- Fetch & Save Product News ---
    product_items = fetch_product_news()
    save_items(product_items)

    # --- Get All Items from DB ---
    db_items = get_items()

    # --- Separate Items by Source for Sectioning ---
    tech_db_items = [item for item in db_items if item['source'] == 'Hacker News']
    product_db_items = [item for item in db_items if item['source'] == 'Product Hunt']

    # --- Summarize AI & Tech News ---
    tech_summaries = []
    for item in tech_db_items:
        prompt = f"Summarize this tech article: {item['title']}. {item['content']}"
        print(f"Sending to Ollama (Tech): {item['title']}")
        summary = query_llm(prompt)
        print(f"Received summary for (Tech): {item['title']}")
        tech_summaries.append(summary)

    # --- Summarize Product News ---
    product_summaries = []
    for item in product_db_items:
        prompt = f"Summarize this product article: {item['title']}. {item['content']}"
        print(f"Sending to Ollama (Product): {item['title']}")
        summary = query_llm(prompt)
        print(f"Received summary for (Product): {item['title']}")
        product_summaries.append(summary)

    # --- Format Digest ---
    tech_section_html = format_section_html("AI & Tech News", tech_db_items, tech_summaries)
    product_section_html = format_section_html("Product News", product_db_items, product_summaries)
    digest_html = tech_section_html + "<br>" + product_section_html

    tech_section_tg = format_section_html_telegram("AI & Tech News", tech_db_items, tech_summaries)
    product_section_tg = format_section_html_telegram("Product News", product_db_items, product_summaries)
    digest_tg = tech_section_tg + "\n" + product_section_tg

    tech_section_md = format_section_markdown("AI & Tech News", tech_db_items, tech_summaries)
    product_section_md = format_section_markdown("Product News", product_db_items, product_summaries)
    digest_md = tech_section_md + "\n" + product_section_md

    # --- Deliver ---
    asyncio.run(send_email("Your Daily Digest", digest_html, text_body=digest_md))
    asyncio.run(send_telegram(digest_tg))
    print("Digest sent via email and Telegram.")

if __name__ == "__main__":
    main()