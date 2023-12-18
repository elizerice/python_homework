def send_mail(email, name, date, place = 'Тюмени' ):
    return(f"To: {email} \n Здравствуйте, {name}! \n Были бы рады видеть вас на встрече начинающих программистов "
     f" в {place}, которая пройдет {date}.")

print(send_mail(email = 'pip@pop.com', name = 'Лиана', date = '12.12.2023', place = 'Москве'))
print(send_mail(email = 'click@pop.com', name = 'Мария', date = '14.12.2023'))
