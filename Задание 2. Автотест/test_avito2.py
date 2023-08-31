from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


def test_add_to_favorite(page):
    page.goto("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
    page.locator("button").filter(has_text="Добавить в избранное").click()
    expect(page.locator("button").filter(has_text="В избранном")).to_be_enabled()
    page.goto("https://www.avito.ru/favorites")
    page.locator("favorite-items-list").get_by_role("link").first.click()
    expect(page).to_have_url("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")


