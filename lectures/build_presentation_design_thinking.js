// Презентация ОП.16: дизайн-мышление и принципы UX/UI (pptxgenjs)
const SKILL = "/root/.claude/skills/synced/036a2070-adda-4f28-8e15-9026d8b9dc82_c917ece7-23d1-4706-b4bb-ad70fbf98a02/pptx";
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(SKILL + "/scripts/apply_theme.js");

const THEME = {
  name: "UX Lecture",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "16202E", lt1: "FFFFFF", dk2: "4A5568", lt2: "EEF2F7",
    accent1: "2A6FA8", accent2: "F2A541", accent3: "3F8F6B", accent4: "B5483A", accent5: "7A5AA6", accent6: "5F6B7A",
    hlink: "2A6FA8", folHlink: "7A5AA6",
  },
};
const HEX = { dark: "16202E", light: "FFFFFF", panel: "EEF2F7", blue: "2A6FA8", amber: "F2A541", muted: "4A5568", rule: "D5DCE6" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Дизайн-мышление и основные принципы UX/UI";
pres.author = "ОП.16, группа 09.02.13";
const C = pres.SchemeColor;
const FOOT = "ОП.16 · 09.02.13 · Дизайн-мышление и UX/UI";
const MX = 0.6, CW = 13.333 - 2 * MX;

function footer(color) {
  return [
    { text: { text: FOOT, options: { x: MX, y: 6.95, w: 8, h: 0.3, fontSize: 11, color, margin: 0 } } },
  ];
}
pres.defineSlideMaster({
  title: "TITLE", background: { color: HEX.dark },
  objects: [{ placeholder: { options: { name: "title", type: "title", x: MX, y: 2.2, w: 11.6, h: 2.2, fontSize: 48, bold: true, color: C.background1, valign: "top", align: "left", margin: 0 }, text: "" } }],
});
pres.defineSlideMaster({
  title: "LIGHT", background: { color: HEX.light },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: MX, y: 0.45, w: CW, h: 1.0, fontSize: 36, bold: true, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
    ...footer(HEX.muted),
  ],
  slideNumber: { x: 12.2, y: 6.95, w: 0.55, h: 0.3, fontSize: 11, color: HEX.muted, align: "right" },
});
pres.defineSlideMaster({
  title: "DARK", background: { color: HEX.dark },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: MX, y: 0.45, w: CW, h: 1.0, fontSize: 36, bold: true, color: C.background1, valign: "middle", align: "left", margin: 0 }, text: "" } },
    ...footer("B6C0CE"),
  ],
  slideNumber: { x: 12.2, y: 6.95, w: 0.55, h: 0.3, fontSize: 11, color: "B6C0CE", align: "right" },
});

let section = null;
function newSlide(master, title, notes, sec) {
  if (sec) { pres.addSection({ title: sec }); section = sec; }
  const s = pres.addSlide({ masterName: master, sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  return s;
}
function card(s, name, x, y, w, h, head, body, o = {}) {
  const dark = o.dark, fill = o.fill || (dark ? C.accent1 : C.background2);
  const txt = o.txt || (dark ? C.background1 : C.text1);
  s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.12, objectName: name + " фон" });
  const runs = [{ text: head, options: { bold: true, fontSize: o.hs || 20, color: o.headColor || txt, breakLine: true, paraSpaceAfter: 6 } }];
  const items = Array.isArray(body) ? body : [body];
  items.forEach((t, i) => runs.push({ text: t, options: { fontSize: o.bs || 16, color: txt, bullet: Array.isArray(body), breakLine: i < items.length - 1, paraSpaceAfter: Array.isArray(body) ? 4 : 0 } }));
  s.addText(runs, { x: x + 0.25, y: y + 0.2, w: w - 0.5, h: h - 0.4, valign: "top", margin: 0, isTextBox: true, objectName: name });
}
function badge(s, n, x, y, d, fill, color, size) {
  s.addShape(pres.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill }, objectName: "Номер " + n });
  s.addText(String(n), { x, y, w: d, h: d, align: "center", valign: "middle", fontSize: size || 18, bold: true, color, margin: 0, isTextBox: true });
}
function band(s, name, y, h, text, fill, color, size) {
  s.addShape(pres.ShapeType.roundRect, { x: MX, y, w: CW, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.12, objectName: name + " фон" });
  s.addText(text, { x: MX + 0.3, y, w: CW - 0.6, h, valign: "middle", fontSize: size || 18, color, margin: 0, isTextBox: true, objectName: name });
}
const rich = (parts, color, size) => parts.map((p, i) => ({ text: p[0], options: { bold: !!p[1], color, fontSize: size } }));

// 1. Титульный
{
  const s = pres.addSlide({ masterName: "TITLE" });
  pres.addSection({ title: "Введение" }); section = "Введение";
  s.addText("ОП.16 · ГРУППА 09.02.13", { x: MX, y: 1.4, w: 8, h: 0.4, fontSize: 16, bold: true, color: C.accent2, charSpacing: 3, margin: 0, isTextBox: true });
  s.addText("Дизайн-мышление и основные принципы UX/UI", { placeholder: "title" });
  s.addText("Лекция для студентов, не знакомых с программированием", { x: MX, y: 4.7, w: 11, h: 0.6, fontSize: 22, color: "B6C0CE", margin: 0, isTextBox: true });
  s.addText("Основные принципы UX/UI для фронтенд-разработки", { x: MX, y: 6.95, w: 9, h: 0.3, fontSize: 11, color: "B6C0CE", margin: 0, isTextBox: true });
  s.addNotes("Приветствие. Тема занятия: как проектировать интерфейсы, исходя из потребностей людей. Программировать сегодня не потребуется: все термины объясняются по ходу лекции.");
}
// 2. План
{
  const s = newSlide("LIGHT", "План занятия", "Занятие делится на три смысловые части: понятия, процесс проектирования и принципы.");
  const items = ["Что такое UX, UI и фронтенд", "Дизайн-мышление и его пять этапов", "Принципы UX: эвристики и законы восприятия", "Принципы UI: иерархия, цвет, шрифты", "Что должен учитывать фронтенд-разработчик", "Пример и роль инструментов ИИ"];
  items.forEach((t, i) => {
    const y = 1.75 + i * 0.82;
    badge(s, i + 1, MX, y, 0.55, HEX.blue, "FFFFFF", 18);
    s.addText(t, { x: MX + 0.85, y, w: 10.5, h: 0.55, valign: "middle", fontSize: 22, color: C.text1, margin: 0, isTextBox: true, objectName: "План " + (i + 1) });
  });
}
// 3. Зачем
{
  const s = newSlide("LIGHT", "Зачем это разработчику", "Подчеркнуть, что курс не требует умения программировать. Принципы одинаковы для любых технологий.");
  const cs = [["Продукт для человека", "Сайт или программа нужны, чтобы человек решил свою задачу. Неудобный продукт не выполняет эту функцию."], ["Фронтенд виден", "Разработчик создаёт то, с чем пользователь работает напрямую, и отвечает за впечатление от продукта."], ["Решения в мелочах", "Сообщение об ошибке, поведение кнопки, вид страницы на телефоне: этого нет в макете, это решает разработчик."]];
  cs.forEach((c, i) => {
    const x = MX + i * 4.1;
    card(s, "Карточка " + (i + 1), x, 1.9, 3.93, 3.5, c[0], c[1], { hs: 22, bs: 18 });
    badge(s, i + 1, x + 0.25, 4.6, 0.5, HEX.amber, HEX.dark, 16);
  });
}
// 4. UX и UI
{
  const s = newSlide("LIGHT", "UX и UI: в чём разница", "Попросить студентов привести свой пример предмета, у которого внешний вид и удобство не совпадают.");
  card(s, "UX", MX, 1.7, 5.95, 2.9, "UX – пользовательский опыт", "Удобно ли человеку достичь цели, быстро ли он справился, доволен ли результатом.", { dark: true, hs: 26, bs: 20 });
  card(s, "UI", MX + 6.18, 1.7, 5.95, 2.9, "UI – пользовательский интерфейс", "Как всё выглядит: расположение элементов, цвета, шрифты, значки, анимация.", { fill: C.accent2, txt: C.text1, hs: 26, bs: 20 });
  band(s, "Пример с дверью", 4.95, 1.7, rich([["Пример с дверью. ", true], ["UI – материал, цвет и ручка. UX – понятно ли без подсказки, тянуть дверь или толкать. Красивая дверь с непонятным открыванием: хороший UI, плохой UX.", false]], HEX.dark, 18), HEX.panel, HEX.dark);
}
// 5. Фронтенд
{
  const s = newSlide("DARK", "Что такое фронтенд", "Аналогия: HTML – каркас и стены здания, CSS – отделка, JavaScript – лифты и электрика. Изучать эти технологии будем в других дисциплинах.");
  s.addText("Видимая часть продукта, которая работает в браузере или на экране устройства. Невидимая часть (сервер и база данных) называется бэкенд.", { x: MX, y: 1.6, w: CW, h: 0.9, fontSize: 20, color: "D5DCE6", margin: 0, isTextBox: true });
  const cs = [["HTML", "Структура страницы: заголовки, абзацы, списки, кнопки, формы."], ["CSS", "Оформление: цвета, шрифты, расположение, подстройка под размер экрана."], ["JavaScript", "Поведение: реакция на нажатия, проверка данных, обновление содержимого."]];
  cs.forEach((c, i) => card(s, c[0], MX + i * 4.1, 2.9, 3.93, 2.7, c[0], c[1], { fill: "223046", txt: "FFFFFF", headColor: "F2A541", hs: 28, bs: 18 }));
}
// 6. Пять этапов
{
  const s = newSlide("LIGHT", "Дизайн-мышление: пять этапов", "Подход развивался в школе дизайна Стэнфордского университета (d.school). Этапы не образуют строгую линию: возвращаться назад нормально.", "Дизайн-мышление");
  s.addText("Подход к решению задач, в центре которого человек, для которого создаётся продукт.", { x: MX, y: 1.55, w: CW, h: 0.5, fontSize: 20, color: C.text2, margin: 0, isTextBox: true });
  const st = ["Эмпатия", "Проблема", "Идеи", "Прототип", "Тестирование"];
  st.forEach((t, i) => {
    const x = MX + i * 2.45;
    s.addShape(pres.ShapeType.roundRect, { x, y: 2.4, w: 2.25, h: 2.0, fill: { color: C.background2 }, line: { color: C.background2 }, rectRadius: 0.12, objectName: "Этап " + (i + 1) + " фон" });
    badge(s, i + 1, x + 0.25, 2.6, 0.6, HEX.blue, "FFFFFF", 22);
    s.addText(t, { x: x + 0.2, y: 3.4, w: 1.95, h: 0.8, valign: "top", fontSize: 17, bold: true, color: C.text1, margin: 0, isTextBox: true, objectName: "Этап " + (i + 1) });
  });
  band(s, "Итеративность", 4.9, 1.3, rich([["Процесс итеративный. ", true], ["Результаты тестирования возвращают команду к предыдущим шагам, и продукт улучшается циклами.", false]], HEX.dark, 20), HEX.amber, HEX.dark);
}
// 7. Эмпатия
{
  const s = newSlide("LIGHT", "Этап 1. Эмпатия", "Пример хорошего вопроса: «Расскажите, как вы в последний раз искали расписание». Плохой вопрос: «Вам ведь удобно, когда расписание на телефоне?»");
  s.addText("Понять чувства, потребности и мотивы человека, взглянув на ситуацию его глазами.", { x: MX, y: 1.55, w: CW, h: 0.5, fontSize: 20, color: C.text2, margin: 0, isTextBox: true });
  card(s, "Методы", MX, 2.3, 7.2, 3.2, "Методы", ["Интервью с открытыми вопросами", "Наблюдение за выполнением задачи", "Анкетирование для проверки гипотез", "Анализ отзывов и обращений"], { hs: 22, bs: 18 });
  card(s, "Ошибки", MX + 7.5, 2.3, 4.63, 3.2, "Типичные ошибки", ["Наводящие вопросы", "Опрос только знакомых", "Свои выводы вместо слов человека"], { fill: C.text1, txt: C.background1, headColor: "F2A541", hs: 22, bs: 18 });
}
// 8. Проблема
{
  const s = newSlide("LIGHT", "Этап 2. Определение проблемы", "Хорошая формулировка описывает потребность, а не готовое решение. Плохо: «Сделать приложение для расписания».");
  card(s, "Персонаж", MX, 1.65, 5.95, 1.9, "Персонаж", "Портрет типичного пользователя по реальным данным: цели и трудности.", { hs: 22, bs: 18 });
  card(s, "Карта пути", MX + 6.18, 1.65, 5.95, 1.9, "Карта пути", "Шаги человека к цели с отметками действий, эмоций и препятствий.", { hs: 22, bs: 18 });
  s.addShape(pres.ShapeType.roundRect, { x: MX, y: 3.85, w: CW, h: 2.8, fill: { color: C.text1 }, line: { color: C.text1 }, rectRadius: 0.12, objectName: "Формула фон" });
  s.addText([
    { text: "Формула проблемы", options: { bold: true, fontSize: 16, color: "F2A541", breakLine: true, paraSpaceAfter: 8 } },
    { text: "«Как нам помочь [кому] достичь [чего], несмотря на [препятствие]?»", options: { bold: true, fontSize: 24, color: "FFFFFF", breakLine: true, paraSpaceAfter: 10 } },
    { text: "Пример: как помочь студенту узнавать об изменениях в расписании в тот же день, не заходя на сайт колледжа?", options: { fontSize: 18, color: "D5DCE6" } },
  ], { x: MX + 0.35, y: 4.05, w: CW - 0.7, h: 2.4, valign: "top", margin: 0, isTextBox: true, objectName: "Формула" });
}
// 9. Идеи
{
  const s = newSlide("LIGHT", "Этап 3. Генерация идей", "Если оценивать идеи сразу, команда отбрасывает необычные варианты и приходит к очевидному. Для разработчика на этом этапе важно оценить осуществимость.");
  s.addText("Сначала идеи порождают, потом отбирают. Нельзя делать это одновременно.", { x: MX, y: 1.55, w: CW, h: 0.5, fontSize: 20, color: C.text2, margin: 0, isTextBox: true });
  card(s, "Порождение", MX, 2.35, 5.95, 3.1, "Порождение", ["Мозговой штурм без критики", "Быстрые наброски на бумаге", "Важно количество идей"], { dark: true, hs: 26, bs: 20 });
  card(s, "Отбор", MX + 6.18, 2.35, 5.95, 3.1, "Отбор", ["Польза для пользователя", "Осуществимость и сроки", "Соответствие проблеме"], { fill: C.accent2, txt: C.text1, hs: 26, bs: 20 });
}
// 10. Прототип
{
  const s = newSlide("LIGHT", "Этап 4. Прототипирование", "Макеты создают в графических редакторах интерфейсов, например в Figma. Разработчик берёт из макета размеры, отступы и цвета.");
  s.addText("Прототип – упрощённая модель продукта для проверки идеи. Ошибку на бумаге исправить дешевле, чем в готовой программе.", { x: MX, y: 1.55, w: CW, h: 0.8, fontSize: 20, color: C.text2, margin: 0, isTextBox: true });
  const cs = [["Низкая детализация", "Эскиз на бумаге, схема экранов. Быстро и дёшево."], ["Средняя детализация", "Цифровой макет с переходами между экранами."], ["Высокая детализация", "Точный макет для передачи разработчику."]];
  cs.forEach((c, i) => card(s, c[0], MX + i * 4.1, 2.6, 3.93, 2.5, c[0], c[1], { hs: 20, bs: 18 }));
  band(s, "Правило", 5.45, 1.1, rich([["Правило: ", true], ["прототип должен быть настолько простым, чтобы его не жалко было выбросить.", false]], HEX.dark, 20), HEX.amber, HEX.dark);
}
// 11. Тестирование
{
  const s = newSlide("DARK", "Этап 5. Тестирование", "Лучше провести несколько небольших раундов с исправлениями между ними, чем один большой. Пример задания: «Найдите расписание своей группы на завтра».");
  s.addText("5", { x: MX, y: 1.6, w: 3.5, h: 3.0, fontSize: 200, bold: true, color: C.accent2, margin: 0, valign: "middle", isTextBox: true, objectName: "Крупная цифра" });
  s.addText("участников выявляют большую часть серьёзных проблем (Я. Нильсен)", { x: MX, y: 4.7, w: 3.9, h: 1.2, fontSize: 18, color: "D5DCE6", margin: 0, valign: "top", isTextBox: true });
  s.addText([
    { text: "Участнику дают задание и наблюдают, не подсказывая.", options: { fontSize: 22, color: "FFFFFF", bold: true, breakLine: true, paraSpaceAfter: 14 } },
    { text: "Удалось ли выполнить задачу", options: { fontSize: 20, color: "E4E8EE", bullet: true, breakLine: true, paraSpaceAfter: 8 } },
    { text: "Сколько времени ушло", options: { fontSize: 20, color: "E4E8EE", bullet: true, breakLine: true, paraSpaceAfter: 8 } },
    { text: "Сколько ошибок допущено", options: { fontSize: 20, color: "E4E8EE", bullet: true, breakLine: true, paraSpaceAfter: 8 } },
    { text: "Где возникло затруднение", options: { fontSize: 20, color: "E4E8EE", bullet: true } },
  ], { x: 5.2, y: 1.9, w: 7.5, h: 3.8, valign: "top", margin: 0, isTextBox: true, objectName: "Что фиксируют" });
}
// 12. Эвристики
{
  const s = newSlide("LIGHT", "Десять эвристик Нильсена", "Эвристики – обобщённые правила оценки удобства (1994 год). Предложить студентам найти нарушение любой из эвристик на знакомом сайте.", "Принципы UX и UI");
  const rows = [["Эвристика", "Пример"], ["1. Видимость состояния", "Индикатор загрузки, «Заказ отправлен»"], ["2. Язык пользователя", "«Корзина», а не «Список позиций»"], ["3. Контроль и свобода", "Кнопки «Назад» и «Отмена»"], ["4. Согласованность", "Одинаковые элементы работают одинаково"], ["5. Предотвращение ошибок", "Подтверждение при удалении"], ["6. Узнавание, не запоминание", "Варианты показаны на экране"], ["7. Гибкость и эффективность", "Поиск, избранное, быстрые действия"], ["8. Минимализм", "Нет лишнего, что отвлекает"], ["9. Помощь с ошибками", "«Пароль короче 8 символов»"], ["10. Справка", "Подсказки там, где они нужны"]];
  const hdr = { bold: true, color: "FFFFFF", fill: { color: HEX.blue }, fontSize: 15, fontFace: "Calibri" };
  const data = rows.map((r, i) => r.map((t) => ({ text: t, options: i === 0 ? hdr : { fontSize: 15, color: HEX.dark, fontFace: "Calibri", fill: { color: i % 2 ? "FFFFFF" : HEX.panel } } })));
  s.addTable(data, { x: MX, y: 1.55, w: CW, colW: [5.2, CW - 5.2], rowH: 0.46, border: { type: "solid", pt: 0.5, color: HEX.rule }, valign: "middle", margin: [0, 0.12, 0, 0.12], objectName: "Таблица эвристик" });
}
// 13. Законы
{
  const s = newSlide("DARK", "Законы восприятия", "Добавить закон близости (принципы Гештальта): рядом расположенные элементы воспринимаются как связанные, поэтому связанные поля формы стоят рядом.");
  const cs = [["Закон Фитса", "Попасть в элемент тем проще, чем он крупнее и ближе. Область нажатия не меньше 44 × 44 пикселей."], ["Закон Хика", "Чем больше вариантов, тем дольше выбор. Ограничивать меню, выделять главное действие."], ["Закон Миллера", "Кратковременная память держит около семи элементов. Информацию делят на небольшие группы."], ["Закон Якоба", "Пользователи ждут, что ваш сайт работает как другие. Корзина справа вверху, логотип ведёт на главную."]];
  cs.forEach((c, i) => card(s, c[0], MX + (i % 2) * 6.18, 1.7 + Math.floor(i / 2) * 2.55, 5.95, 2.35, c[0], c[1], { fill: "223046", txt: "E4E8EE", headColor: "F2A541", hs: 22, bs: 17 }));
}
// 14. UI
{
  const s = newSlide("LIGHT", "Принципы UI", "Проверка иерархии: прищуриться и посмотреть на экран. Должно остаться понятным, что главное. Пустое пространство не «потерянное место», оно отделяет блоки и облегчает чтение.");
  const cs = [["Визуальная иерархия", "Взгляд идёт от главного к второстепенному: размер, цвет, контраст, расположение."], ["Сетка и воздух", "Выравнивание по общим линиям и свободное пространство между блоками."], ["Цвет и контраст", "Основной, акцентный и нейтральные цвета. Контраст текста и фона не ниже 4,5 к 1."], ["Типографика", "Два-три шрифта, основной текст от 16 пикселей, строка 50–75 символов."]];
  cs.forEach((c, i) => card(s, c[0], MX + (i % 2) * 6.18, 1.65 + Math.floor(i / 2) * 2.1, 5.95, 1.95, c[0], c[1], { hs: 22, bs: 17, headColor: C.accent1 }));
  band(s, "Цвет и смысл", 5.95, 0.8, rich([["Не передавайте смысл только цветом: ", true], ["добавляйте текст или значок.", false]], HEX.dark, 18), HEX.amber, HEX.dark);
}
// 15. Обязанности
{
  const s = newSlide("LIGHT", "За что отвечает фронтенд-разработчик", "Макет обычно показывает только обычное состояние элементов. Остальные разработчик продумывает сам, опираясь на принципы согласованности и обратной связи.");
  const rs = [["Адаптивность", "Страница подстраивается под телефон, планшет и компьютер. Сначала проектируют для малого экрана."], ["Скорость", "Сжатые изображения, нет лишней загрузки, индикатор ожидания."], ["Доступность", "Контраст, подписи к изображениям, управление с клавиатуры."], ["Формы", "Подписи у полей, понятные ошибки рядом с полем, сохранение введённого."], ["Состояния", "Обычное, наведение, нажатие, ошибка, недоступно: каждое различимо."]];
  rs.forEach((r, i) => {
    const y = 1.6 + i * 1.03;
    s.addShape(pres.ShapeType.roundRect, { x: MX, y, w: CW, h: 0.9, fill: { color: C.background2 }, line: { color: C.background2 }, rectRadius: 0.1, objectName: r[0] + " фон" });
    s.addText(r[0], { x: MX + 0.3, y, w: 2.7, h: 0.9, valign: "middle", fontSize: 20, bold: true, color: C.accent1, margin: 0, isTextBox: true, objectName: r[0] });
    s.addText(r[1], { x: MX + 3.1, y, w: CW - 3.4, h: 0.9, valign: "middle", fontSize: 16, color: C.text1, margin: 0, isTextBox: true, objectName: r[0] + " описание" });
  });
}
// 16. Пример
{
  const s = newSlide("LIGHT", "Пример: расписание колледжа", "Сопоставить с принципами: блок изменений наверху (иерархия), крупная кнопка (закон Фитса), сохранение выбора (меньше шагов), контраст и крупный шрифт (мобильное использование). Пример учебный.", "Практика");
  const rows = [["Этап", "Что сделали"], ["Эмпатия", "Интервью с шестью студентами: расписание ищут на телефоне, сайт грузится медленно"], ["Проблема", "Как помочь студенту узнать об изменениях в тот же день?"], ["Идеи", "Уведомления, виджет, бот, страница с блоком «Изменения сегодня»"], ["Прототип", "Бумажный эскиз, затем макет: изменения наверху, ниже выбор группы"], ["Тест", "Двое из пяти не заметили выбор группы: кнопку увеличили, выбор сохраняют"]];
  const hdr = { bold: true, color: "FFFFFF", fill: { color: HEX.blue }, fontSize: 16, fontFace: "Calibri" };
  const data = rows.map((r, i) => r.map((t, j) => ({ text: t, options: i === 0 ? hdr : { fontSize: 16, bold: j === 0, color: HEX.dark, fontFace: "Calibri", fill: { color: i % 2 ? "FFFFFF" : HEX.panel } } })));
  s.addTable(data, { x: MX, y: 1.7, w: CW, colW: [2.2, CW - 2.2], rowH: 0.72, border: { type: "solid", pt: 0.5, color: HEX.rule }, valign: "middle", margin: [0, 0.15, 0, 0.15], objectName: "Таблица примера" });
}
// 17. ИИ
{
  const s = newSlide("LIGHT", "Роль инструментов ИИ", "Связь со специальностью 09.02.13: инструменты искусственного интеллекта применяют как помощников, но решение и проверка остаются за специалистом.");
  card(s, "Помогают", MX, 1.65, 5.95, 3.5, "Помогают", ["Обобщать записи интервью и отзывы", "Предлагать формулировки проблемы", "Создавать черновые макеты и тексты", "Подсказывать идеи для обсуждения"], { dark: true, hs: 26, bs: 18 });
  card(s, "Не заменяют", MX + 6.18, 1.65, 5.95, 3.5, "Не заменяют", ["Наблюдение за реальными людьми", "Проверку удобства на пользователях", "Ответственность за решение"], { fill: C.text1, txt: C.background1, headColor: "F2A541", hs: 26, bs: 18 });
  band(s, "Правило ИИ", 5.5, 0.9, rich([["Правило: ", true], ["результат ИИ проверяют на пользователях и на соответствие принципам UX/UI.", false]], HEX.dark, 18), HEX.amber, HEX.dark);
}
// 18. Главное
{
  const s = newSlide("DARK", "Главное", "Итог занятия. Напомнить практическое задание: интервью с двумя одногруппниками, формулировка проблемы, эскиз экрана.");
  const items = [["UX", " – удобство для человека, ", "UI", " – внешний вид и поведение элементов"], ["Дизайн-мышление: ", "пять этапов", ", процесс повторяется циклами", ""], ["Решение проверяют на ", "реальных пользователях", "", ""], ["Принципы: ", "эвристики", ", законы восприятия, иерархия, контраст", ""], ["Фронтенд отвечает за ", "адаптивность, скорость, доступность", "", ""]];
  const lines = [
    [["UX", true], [" – удобство для человека, ", false], ["UI", true], [" – внешний вид и поведение элементов", false]],
    [["Дизайн-мышление: ", false], ["пять этапов", true], [", процесс повторяется циклами", false]],
    [["Решение проверяют на ", false], ["реальных пользователях", true]],
    [["Принципы: ", false], ["эвристики", true], [", законы восприятия, иерархия, контраст", false]],
    [["Фронтенд отвечает за ", false], ["адаптивность, скорость, доступность", true]],
  ];
  lines.forEach((ln, i) => {
    const y = 1.7 + i * 0.98;
    badge(s, i + 1, MX, y, 0.55, HEX.amber, HEX.dark, 18);
    s.addText(ln.map(([t, b]) => ({ text: t, options: { bold: b, color: b ? "F2A541" : "FFFFFF", fontSize: 22 } })), { x: MX + 0.85, y, w: 11, h: 0.55, valign: "middle", margin: 0, isTextBox: true, objectName: "Вывод " + (i + 1) });
  });
}
// 19. Вопросы
{
  const s = newSlide("LIGHT", "Вопросы и задание", "Остальные контрольные вопросы приведены в тексте лекции.");
  const qs = ["Чем UX отличается от UI?", "Назовите пять этапов дизайн-мышления.", "Почему процесс называют итеративным?", "Что такое персонаж и карта пути?", "Объясните закон Фитса и закон Хика."];
  qs.forEach((t, i) => {
    const y = 1.6 + i * 0.72;
    badge(s, i + 1, MX, y, 0.5, HEX.blue, "FFFFFF", 16);
    s.addText(t, { x: MX + 0.8, y, w: 11, h: 0.5, valign: "middle", fontSize: 20, color: C.text1, margin: 0, isTextBox: true, objectName: "Вопрос " + (i + 1) });
  });
  band(s, "Практика", 5.4, 1.3, rich([["Практика: ", true], ["выберите знакомый сервис, проведите интервью с двумя одногруппниками, сформулируйте проблему «Как нам помочь…» и нарисуйте эскиз главного экрана.", false]], HEX.dark, 18), HEX.amber, HEX.dark);
}

(async () => {
  const out = process.argv[2];
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("ok", out);
})();
