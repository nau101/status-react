import pytest

from tests import marks, common_password, get_current_time, group_chat_users
from tests.base_test_case import SingleDeviceTestCase, MultipleDeviceTestCase
from views.sign_in_view import SignInView


@marks.all
@marks.account
class TestAccountSingleDevice(SingleDeviceTestCase):

    @marks.testrail_id(758)
    def test_create_account(self):
        if not self.test_fairy_warning_is_shown:
            self.errors.append('TestFairy warning is not shown')
        sign_in = SignInView(self.driver)
        if not sign_in.i_have_account_button.is_element_displayed():
            self.errors.append("'I have an account' button is not displayed")
        sign_in.create_account_button.click()
        sign_in.password_input.set_value(common_password)
        sign_in.next_button.click()
        sign_in.confirm_password_input.set_value(common_password)
        sign_in.next_button.click()

        sign_in.element_by_text_part('Display name').wait_for_element(30)
        sign_in.name_input.send_keys('user_%s' % get_current_time())

        sign_in.next_button.click()
        if not sign_in.learn_more_link.is_element_displayed(10):
            self.errors.append("'Learn more about what we collect' is not shown")
        if not sign_in.share_data_button.is_element_displayed(10):
            self.errors.append("'Share data' button is not visible")
        if not sign_in.do_not_share_button.is_element_displayed(10):
            self.errors.append("'Do not share' button is not visible")
        self.verify_no_errors()

    @marks.testrail_id(760)
    def test_set_profile_picture(self):
        sign_in_view = SignInView(self.driver)
        sign_in_view.create_user()
        profile_view = sign_in_view.profile_button.click()
        profile_view.edit_profile_picture(file_name='sauce_logo.png')
        profile_view.home_button.click()
        sign_in_view.profile_button.click()
        profile_view.swipe_down()
        if not profile_view.profile_picture.is_element_image_equals_template():
            pytest.fail('Profile picture was not updated')

    @marks.testrail_id(1403)
    def test_share_contact_code_and_wallet_address(self):
        sign_in_view = SignInView(self.driver)
        sign_in_view.create_user()
        profile_view = sign_in_view.profile_button.click()
        profile_view.share_my_contact_key_button.click()
        profile_view.share_button.click()
        if not profile_view.element_by_text('Share with').is_element_displayed():
            self.errors.append('Can\'t share contact code')
        profile_view.click_system_back_button()
        profile_view.cross_icon.click()
        wallet = profile_view.wallet_button.click()
        wallet.set_up_wallet()
        request = wallet.request_button.click()
        request.share_button.click()
        if not profile_view.element_by_text('Share with').is_element_displayed():
            self.errors.append('Can\'t share wallet address')
        self.verify_no_errors()
