# import imaplib
# import email
# import time
# import re
# from email import message_from_bytes
#
#
# class Mailchecker:
#     def __init__(self,
#                  login="manikosto@gmail.com",
#                  password="nhcq dfig",
#                  email_service="imap.gmail.com",
#                  subject_for_deletion=""):
#         try:
#             self.mail = imaplib.IMAP4_SSL(email_service)  # Создание защищенного IMAP соединения
#             self.mail.login(login, password)  # Вход в почтовый аккаунт
#             print("Успешное подключение к почте.")
#
#             if subject_for_deletion:
#                 self.delete_emails_with_subject(subject_for_deletion)  # Удаление писем с частичным совпадением темы
#         except imaplib.IMAP4.error as e:
#             print(f"Ошибка при подключении: {e}")
#
#     def search_emails(self,
#                       partial_subject,
#                       regex_pattern="https:\/\/demo\.opensource-socialnetwork\.org\/uservalidate\/activate\/\d+\/[a-f0-9]{32}",
#                       folder="inbox",
#                       timeout=90,
#                       check_frequency=8):
#         start_time = time.time()
#
#         try:
#             while (time.time() - start_time) < timeout:
#                 self.mail.select(folder)  # Выбор папки для поиска
#                 query = f'(SUBJECT "{partial_subject}")'
#                 result, data = self.mail.search(None, query)
#
#                 if data[0]:  # Если найдены письма
#                     for email_id in data[0].split():
#                         result, data = self.mail.fetch(email_id, "(RFC822)")  # Получение данных письма
#                         if result != 'OK':
#                             continue
#
#                         msg = message_from_bytes(data[0][1])  # Преобразование данных письма в объект сообщения
#
#                         # Обработка многочастных писем
#                         if msg.is_multipart():
#                             for part in msg.walk():
#                                 if part.get_content_type() in ['text/plain', 'text/html']:
#                                     body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
#
#                                     # Логируем тело письма для отладки
#                                     print(f"Тело письма: {body}")
#
#                                     match = re.search(regex_pattern, body, re.DOTALL)
#                                     if match:
#                                         print("Соответствие найдено.")
#                                         self.close_connection()  # Закрываем соединение
#                                         return match.group()  # Возвращаем найденную ссылку
#                         else:
#                             body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
#                             print(f"Тело письма (простое): {body}")  # Логируем для отладки
#                             match = re.search(regex_pattern, body, re.DOTALL)
#                             if match:
#                                 print("Соответствие найдено.")
#                                 self.close_connection()  # Закрываем соединение
#                                 return match.group()  # Возвращаем найденную ссылку
#                 else:
#                     print(f"Писем с темой, содержащей '{partial_subject}', не найдено.")
#
#                 time.sleep(check_frequency)  # Ожидание перед следующей проверкой
#         except imaplib.IMAP4.error as e:
#             print(f"Ошибка при поиске писем: {e}")
#             self.close_connection()  # Закрываем соединение при ошибке
#
#         print("Поиск завершен, ничего не найдено.")
#         self.close_connection()  # Закрываем соединение, если ничего не найдено
#         return None
#
#     def delete_emails_with_subject(self, partial_subject, folder="inbox"):
#         try:
#             self.mail.select(folder)  # Выбор папки
#             query = f'(SUBJECT "{partial_subject}")'
#             result, data = self.mail.search(None, query)
#             if result == 'OK':
#                 for num in data[0].split():
#                     self.mail.store(num, '+FLAGS', '\\Deleted')  # Пометка писем как удаленных
#                 self.mail.expunge()  # Окончательное удаление помеченных писем
#                 print(f"Письма с темой, содержащей '{partial_subject}', удалены.")
#             else:
#                 print(f"Писем с темой, содержащей '{partial_subject}', не найдено.")
#         except imaplib.IMAP4.error as e:
#             print(f"Ошибка при удалении писем: {e}")
#
#     def close_connection(self):
#         try:
#             self.mail.logout()  # Завершение сессии
#             print("Подключение к почте закрыто.")
#         except imaplib.IMAP4.error as e:
#             print(f"Ошибка при закрытии подключения: {e}")
#
#
# # subject = "Something"
# #
# # mail = Mailchecker(login="fanisov86@gmail.com", password="gkwf dcom qact lrkt", subject_for_deletion=subject)
# # link_regex = r'https:\/\/vk\.com\/\S*|href="(https:\/\/vk\.com\/\S*)"'  # Обновленное регулярное выражение для захвата всех ссылок на vk.com
# # print(mail.search_emails(subject, link_regex))