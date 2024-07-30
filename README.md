<h1>Тестирование WebCalculator</h1>

<p>Этот проект содержит автоматизированные тесты для приложения WebCalculator, серверного калькулятора, выполняющего арифметические операции с целыми числами через HTTP-API.</p>

<h2>Обзор проекта</h2>

<p>Приложение WebCalculator (<code>webcalculator.exe</code>) позволяет выполнять арифметические операции с целыми числами на стороне сервера и возвращает результаты клиенту. Взаимодействие между клиентом и сервером осуществляется через HTTP-API.</p>

<h3>Поддерживаемые операции</h3>
<ul>
    <li>Сложение двух чисел</li>
    <li>Умножение двух чисел</li>
    <li>Целочисленное деление</li>
    <li>Получение остатка от деления</li>
</ul>

<h2>Набор тестов</h2>

<p>Набор тестов написан на Python 3.x и охватывает следующие аспекты приложения WebCalculator:</p>

<ul>
    <li>Проверка формата запросов/ответов API для всех указанных методов API</li>
    <li>Тестирование основной функциональности: точность вычислений с допустимыми входными данными</li>
    <li>Негативное тестирование (проверка кодов ошибок)</li>
    <li>Тестирование управления приложением: изменение хоста/порта, значения по умолчанию, функциональность остановки/перезапуска</li>
</ul>

<h3>Дополнительные тесты</h3>
<ul>
    <li>Негативное тестирование (проверка кодов ошибок)</li>
    <li>Автоматическая генерация отчета о тестировании</li>
</ul>

<h2>Управление приложением</h2>

<p>Приложение WebCalculator управляется через командную строку:</p>

<ul>
    <li><strong>Запуск:</strong> <code>webcalculator.exe start [host] [port]</code>
        <ul>
            <li>Если порт не указан, используется порт по умолчанию (17678)</li>
            <li>Если хост не указан, используется адрес по умолчанию (127.0.0.1)</li>
        </ul>
    </li>
    <li><strong>Остановка:</strong> <code>webcalculator.exe stop</code></li>
    <li><strong>Перезапуск:</strong> <code>webcalculator.exe restart</code></li>
    <li><strong>Просмотр лога:</strong> <code>webcalculator.exe show_log</code></li>
    <li><strong>Справка:</strong> <code>webcalculator.exe --h</code> или <code>webcalculator.exe --help</code></li>
</ul>

<h2>API калькулятора</h2>

<p>API калькулятора доступно по адресу <code>http://host:port/api/имя_задачи</code></p>

<h3>Доступные задачи:</h3>
<ul>
    <li><code>state</code> - Проверка состояния сервера (GET)</li>
    <li><code>addition</code> - Сложение x и y (POST)</li>
    <li><code>multiplication</code> - Умножение x и y (POST)</li>
    <li><code>division</code> - Деление на цело x на y (POST)</li>
    <li><code>remainder</code> - Остаток от деления x на y (POST)</li>
</ul>

<p>Для задач типа POST тело запроса должно содержать JSON с ключами "x" и "y", и значениями типа integer.</p>

<pre><code>{"x": 42, "y": 24}</code></pre>

<h3>Формат ответа:</h3>
<ul>
    <li>Успешный ответ: <code>{"statusCode": 0, "result": результат_операции}</code></li>
    <li>Ответ с ошибкой: <code>{"statusCode": код_ошибки, "statusMessage": "сообщение_об_ошибке"}</code></li>
</ul>

<p>Коды ошибок:</p>
<ul>
    <li>0 - Все хорошо</li>
    <li>1 - Ошибка вычисления</li>
    <li>2 - Не хватает ключей в теле запроса</li>
    <li>3 - Одно из значений не является целым числом</li>
    <li>4 - Превышен размер одного из значений</li>
    <li>5 - Неправильный формат тела запроса</li>
</ul>
