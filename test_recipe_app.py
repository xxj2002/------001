from playwright.sync_api import sync_playwright

def test_recipe_generation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("正在访问菜谱生成系统...")
        page.goto('http://localhost:5173')
        page.wait_for_load_state('networkidle')

        print("页面加载成功，截图保存...")
        page.screenshot(path='F:/菜谱系统/菜谱生成系统001/test_screenshots/page_load.png', full_page=True)

        print("\n检查页面关键元素...")

        page.wait_for_timeout(2000)

        breakfast_label = page.locator('text=早餐').first
        if breakfast_label:
            print("✓ 找到'早餐'标签")

        lunch_label = page.locator('text=午餐').first
        if lunch_label:
            print("✓ 找到'午餐'标签")

        dinner_label = page.locator('text=晚餐').first
        if dinner_label:
            print("✓ 找到'晚餐'标签")

        night_snack_label = page.locator('text=夜宵').first
        if night_snack_label:
            print("✓ 找到'夜宵'标签")

        morning_snack_label = page.locator('text=课间餐').first
        if morning_snack_label:
            print("✓ 找到'课间餐'标签")

        print("\n尝试生成菜谱...")
        generate_button = page.locator('button:has-text("生成")').first
        if generate_button:
            generate_button.click()
            print("✓ 点击了'生成'按钮")
            page.wait_for_timeout(3000)
            page.screenshot(path='F:/菜谱系统/菜谱生成系统001/test_screenshots/after_generate.png', full_page=True)
            print("✓ 截图已保存")

        print("\n检查菜品标签是否正确显示...")
        lunch_main_labels = page.locator('text=午餐主荤菜').all()
        print(f"找到 {len(lunch_main_labels)} 个'午餐主荤菜'标签")

        side_labels = page.locator('text=副荤菜').all()
        print(f"找到 {len(side_labels)} 个'副荤菜'标签")

        breakfast_labels = page.locator('text=稀饭, text=馒头, text=花卷, text=蛋类, text=叶菜, text=根茎菜, text=豆类').all()
        print(f"找到 {len(breakfast_labels)} 个早餐相关标签")

        print("\n测试完成!")
        browser.close()

if __name__ == "__main__":
    test_recipe_generation()
