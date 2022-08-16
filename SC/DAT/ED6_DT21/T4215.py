import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4215_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4215   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4215.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '吉尔维厨师长',
            x                   = -68800,
            z                   = 0,
            y                   = 73020,
            direction           = 284,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '福鲁克',
            x                   = -70370,
            z                   = 0,
            y                   = 69400,
            direction           = 356,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '里吉斯',
            x                   = -70550,
            z                   = 0,
            y                   = 74650,
            direction           = 173,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x11A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_133',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_181')

    def _loc_133(): pass

    label('loc_133')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13D',
    )

    Jump('loc_181')

    def _loc_13D(): pass

    label('loc_13D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_147',
    )

    Jump('loc_181')

    def _loc_147(): pass

    label('loc_147')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_181',
    )

    ChrSetPos(0x0008, -61660, 0, 68030, 87)
    ChrSetPos(0x0009, -70230, 0, 65550, 181)
    ChrSetPos(0x000A, -69850, 0, 77540, 273)

    def _loc_181(): pass

    label('loc_181')

    Return()

# id: 0x0001 offset: 0x182
@scena.Code('func_01_182')
def func_01_182():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19E',
    )

    OP_B1('t4215_y')

    Jump('loc_1A7')

    def _loc_19E(): pass

    label('loc_19E')

    OP_B1('t4215_n')

    def _loc_1A7(): pass

    label('loc_1A7')

    Return()

# id: 0x0002 offset: 0x1A8
@scena.Code('func_02_1A8')
def func_02_1A8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_22E',
    )

    ChrTalk(
        0x00FE,
        (
            '用炭火和暖炉烹调也\n',
            '别有风味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无法解决的问题恐怕\n',
            '就是费时这一点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来暂时是没法做出\n',
            '像样的饭菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF')

    def _loc_22E(): pass

    label('loc_22E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2C3',
    )

    ChrTalk(
        0x00FE,
        (
            '在离宫进行的签字仪式上\n',
            '将会举办宴会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在搭配\n',
            '餐室的菜单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了使条约的签字顺利进行，\n',
            '我会竭尽自己的的力量认真工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF')

    def _loc_2C3(): pass

    label('loc_2C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2FF',
    )

    ChrTalk(
        0x00FE,
        (
            '祝科洛蒂娅殿下\n',
            '心情愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '您来这里有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FF(): pass

    label('loc_2FF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x303
@scena.Code('func_03_303')
def func_03_303():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_36E',
    )

    ChrTalk(
        0x00FE,
        (
            '签字仪式的宴会\n',
            '获得了相当的好评哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每个国家的代表都很高兴地\n',
            '品尝了厨师长做的菜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_475')

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_425',
    )

    ChrTalk(
        0x00FE,
        (
            '在签字仪式当日的前一天他\n',
            '就去离宫进行烹调了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为有很多大人物要来，\n',
            '必须好好地管理食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是出现食物中毒那就是国际问题了，\n',
            '最重要的是这关系到厨师的名声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_475')

    def _loc_425(): pass

    label('loc_425')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_475',
    )

    ChrTalk(
        0x00FE,
        (
            '厨师长会做上千种菜，\n',
            '确实是个了不起的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我必须好好跟着学……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_475(): pass

    label('loc_475')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x479
@scena.Code('func_04_479')
def func_04_479():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4DC',
    )

    ChrTalk(
        0x00FE,
        (
            '如果仅仅是烫和煮的话\n',
            '用火也没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '火候的掌握果然\n',
            '不像用导力器那么方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58F')

    def _loc_4DC(): pass

    label('loc_4DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_515',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……不能\n',
            '漏买东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来要忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58F')

    def _loc_515(): pass

    label('loc_515')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_58F',
    )

    ChrTalk(
        0x00FE,
        (
            '下水道的门关上了之后\n',
            '储藏室的老鼠总算少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，真受不了\n',
            '那些咬坏别人辛辛苦苦\n',
            '搬运进去的食品的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_58F(): pass

    label('loc_58F')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
