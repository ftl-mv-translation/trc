from snippets.mass_edits import mass_translate

REPLACE_MAP = {
    "You power up the machine to max and watch as a rift opens, shaking the ship until suddenly it powers off, and a flashing green light followed by a string of coordinates signifies that it has worked.": "Вы включаете машину на полную мощность и наблюдаете, как открывается разлом, тряся корабль. Затем она внезапно отключается, и мигающий зелёный свет вместе с строчкой координат информирует вас о том, что это сработало.",
    "Draw straws and send over a crew as tribute.": "Вытянуть жребий и отправить одного из членов экипажа в качестве дани.",
    "Servant": "Слуга",
    "They stay outside your weapons range, and eventually jump away.": "Они остаются за пределами досягаемости ваших орудий и, спустя время, уходят в прыжок.",
    "DECKHANDS": "ЭКИПАЖ",
    "Mod. Ion": "Мод. ион",
    "Mod. Laser": "Мод. лазер",
    "Modular Ion": "Модульный ион",
    "Modular Laser": "Модульный лазер",
    "Music Unlocked.": "Разблокирована музыка.",
    "Success!": "Успех!",
    "AUXILIARY SYSTEMS": "ДОПОЛНИТЕЛЬНЫЕ СИСТЕМЫ",
    "Continue with the jump.": "Продолжить прыжок.",
    "Detach the modules.": "Отсоединить модули.",
    "ESSENTIAL SYSTEMS": "ОСНОВНЫЕ СИСТЕМЫ",
    "You prepare to jump to the new co-ordinates, and change your flight path accordingly.": "Вы готовитесь прыгнуть на новые координаты и меняете маршрут корабля соответствующим образом.",
    "Your Morph transforms back to its original shape.": "Ваш Морф возвращает свою изначальную форму.",
    "Avoid the ship.": "Обойти корабль.",
    "Accept their surrender.": "Принять их капитуляцию.",
    "Agree.": "Согласиться.",
    "You prepare to secure their cargo by force.": "Вы готовитесь захватить их груз силой.",
    "Accept.": "Принять.",
    "Hail them.": "Выйти с ними на связь.",
    "You're also surprised to find a special weapon amongst the wreckage! You've never seen a weapon like this before, so you assume it's a custom model made by the renegades themselves.": "К вашему удивлению, вы также находите в обломках особое оружие! Вы ещё никогда такого не видели, так что вы предполагает, что это нестандартная модель, изготовленная самими ренегатами.",
    "Attack!": "Атаковать!",
    "Go back.": "Вернуться.",
    "???": "???",
    "Multiverse Renegade": "Ренегат мультивселенной",
    "No thanks.": "Нет, спасибо.",
    "Contact Federation command.": "Связаться с командным пунктом Федерации.",
    "YOU SHOULD NEVER SEE THIS.": "ВЫ НИКОГДА НЕ ДОЛЖНЫ ЭТО ВИДЕТЬ.",
    "Do something else instead.": "Заняться чем-то другим.",
    "No weapon has ever sparked a larger ethical controversy, but if it works it works.": "Ни одно оружие не сравнится с этим по этической противоречивости, но что работает, то работает.",
    "Fortunately, the MV ship accepts the tribute in turn for letting you live.": "К счастью, МВ-корабль принимает дань взамен на вашу жизнь.",
    "Continue to the fight!": "Перейти к битве!",
    "Ignore them.": "Игнорировать их.",
    "Reroute.": "Перенаправить.",
    "Are you sure you want to change the drone's settings?": "Вы уверены, что хотите изменить настройки дрона?",
    "Your Morph transforms into a new shape.": "Ваш Морф меняет форму.",
    "Though your crew's memories have been almost completely erased, they remember enough to at least remain loyal to the Federation.": "Хотя воспоминания члена экипажа практически полностью стёрты, он помнит достаточно, чтобы хотя бы оставаться верным Федерации.",
    "(Clone Bay) Revive your crew.": "(Клон-отсек) Оживить своего члена экипажа.",
    "Projectile": "Снаряд",
    "Reset the cannon.": "Сбросить параметры пушки.",
    "You finish resetting the weapon.": "Вы завершаете сброс параметров оружия.",
    "You reset the weapon.": "Вы сбрасываете параметры оружия.",
    "You install the modification.": "Вы устанавливаете модификацию.",
    "Are you sure? You will not be able to retrieve them without a Clone Bay, and all skills will be lost.": "Вы уверены? Вы не сможете их вернуть без клон-отсека, и все навыки будут потеряны.",
    "Exit hyperspeed.": "Выйти из гиперскорости.",
    "You finish the process.": "Вы завершаете процедуру.",
    "You start the process.": "Вы начинаете процедуру.",
    "Your crew cannot be cloned on your ship as they are inside the cannon.": "Вы не можете клонировать членов экипажа на своём корабле, так как они находятся внутри пушки.",
    "You install the upgrade.": "Вы устанавливаете улучшение.",
    "Leave.": "Уйти.",
    "Detach both modules.": "Отключить оба модуля.",
    "Renegade Cruiser": "Крейсер ренегата",
    "Return to the toggle menu.": "Вернуться в меню переключения.",
    "Refuse.": "Отказать.",
    "Nevermind, do something else.": "Неважно, заняться чем-то ещё.",
    "No.": "Нет.",
    "You finish calibrating the drone successfully.": "Вы успешно завершаете калибровку дрона.",
    "You start calibrating the drone...": "Вы начинаете калибровку дрона...",
    "Yes.": "Да.",
    "Decline.": "Отказать.",
    "YOU SHOULD NEVER SEE THIS": "ВЫ НИКОГДА НЕ ДОЛЖНЫ ЭТО ВИДЕТЬ",
    "Use your blessing to avoid combat.": "Использовать благословение, чтобы избежать битвы.",
    "Do something on-board the ship.": "Заняться чем-либо на корабле.",
    "Explored location. Nothing left of interest.": "Посещённое место. Ничего интересного.",
    "An unvisited location.": "Непосещённое место.",
    "Check the storage.": "Проверить склад.",
    "Nevermind.": "Неважно.",
    "Do something onboard the ship.": "Заняться чем-либо на корабле.",
    "...": "...",
    "Do nothing.": "Ничего не делать.",
    "Continue...": "Продолжить...",
}

mass_translate('locale/**/ru.po', REPLACE_MAP, overwrite=True)