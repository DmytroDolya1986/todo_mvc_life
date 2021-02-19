from selene.support.shared import browser
from selene import have


def test_todo_lifecycle():

    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length === 39;'))

    browser.element('#new-todo').set_value('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list li').element_by(have.exact_text('c')).double_click()
    browser.all('#todo-list li').element_by(have.css_class('editing')).element('.edit').type(' edited').press_enter()

    browser.all('#todo-list li').element_by(have.exact_text('c edited')).element('.toggle').click()

    browser.element('#clear-completed').click()
    browser.all('#todo-list li').should(have.exact_texts('a', 'b'))

    browser.all('#todo-list li').element_by(have.exact_text('b')).double_click()
    browser.all('#todo-list li').element_by(have.css_class('editing')).element('.edit').type(' > to be cancelled').press_escape()

    browser.all('#todo-list li').element_by(have.exact_text('b')).hover().element('.destroy').click()
    browser.all('#todo-list li').should(have.exact_texts('a'))

    browser.clear_local_storage()
