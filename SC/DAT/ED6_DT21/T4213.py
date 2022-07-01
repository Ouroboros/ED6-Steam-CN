import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4213_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4213   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '尤莉亚上尉'),
    TXT(0x02, '亲卫队队员'),
    TXT(0x03, '亲卫队队员'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4213.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x892
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 74150,
            z                   = 0,
            y                   = -35040,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 64650,
            z                   = 0,
            y                   = -33590,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 70330,
            z                   = 0,
            y                   = -41620,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x11A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_12E',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    Jump('loc_14E')

    def _loc_12E(): pass

    label('loc_12E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_138',
    )

    Jump('loc_14E')

    def _loc_138(): pass

    label('loc_138')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_147',
    )

    ClearChrFlags(0x0008, 0x0080)

    Jump('loc_14E')

    def _loc_147(): pass

    label('loc_147')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_14E',
    )

    def _loc_14E(): pass

    label('loc_14E')

    Return()

# id: 0x0001 offset: 0x14F
@scena.Code('Init')
def Init():
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
        'loc_16B',
    )

    OP_B1('t4213_y')

    Jump('loc_174')

    def _loc_16B(): pass

    label('loc_16B')

    OP_B1('t4213_n')

    def _loc_174(): pass

    label('loc_174')

    Return()

# id: 0x0002 offset: 0x175
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_198',
    )

    OP_8D(0x00FE, 62680, -31070, 69060, -36680, 2000)

    Jump('ReInit')

    def _loc_198(): pass

    label('loc_198')

    Return()

# id: 0x0003 offset: 0x199
@scena.Code('func_03_199')
def func_03_199():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1BC',
    )

    OP_8D(0x00FE, 65860, -37440, 73950, -46540, 2000)

    Jump('func_03_199')

    def _loc_1BC(): pass

    label('loc_1BC')

    Return()

# id: 0x0004 offset: 0x1BD
@scena.Code('func_04_1BD')
def func_04_1BD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_5F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CD, 0, 0x1668)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50C',
    )

    ChrTalk(
        0x0008,
        (
            '#0100271450V#173F科洛蒂娅殿下……\n',
            '艾丝蒂尔也在一起啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271451V#1008F这次是被尤莉亚上尉\n',
            '和亲卫队给救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100271452V#171F呵呵，这是因为有了希德中校\n',
            '那迅速又恰当的判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271453V#176F而且如果凯文先生不在的话\n',
            '我们也来不及追上凯诺娜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271454V#1002F凯诺娜上尉啊……\n',
            '她现在在雷斯顿要塞？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271455V她好像愿意说出玲和\n',
            '结社的事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100271456V#170F凯诺娜她明白现在的危急情况\n',
            '以及自己的作用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271457V她需要的是一种契机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271458V#1011F……这样啊，你认识她，\n',
            '难怪这么了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0100271459V#170F我和她在士官学校时代\n',
            '曾是互相竞争和提高的关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271460V在我被配属到亲卫队、\n',
            '她被配属到情报部之后\n',
            '应该也没改变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271461V#176F现在想来，说不定正因为有了她，\n',
            '才有了现在的我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271462V#178F我……从没想到结果\n',
            '会是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060271463V#042F尤莉亚上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1668)

    Jump('loc_5F6')

    def _loc_50C(): pass

    label('loc_50C')

    ChrTalk(
        0x0008,
        (
            '#0100271464V#170F还有结社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271465V#176F执行者们的能力自不必说，竟然\n',
            '还拥有制造出那个巨大机器人的技术能力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271466V#170F看来我们的敌人\n',
            '比想象中的强大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100271467V虽然我们以前并没有轻视他们，\n',
            '不过还是要重新认识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F6(): pass

    label('loc_5F6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x5FA
@scena.Code('func_05_5FA')
def func_05_5FA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_659',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯地区真的\n',
            '出现了龙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军的飞船竟然和龙战斗了，\n',
            '看来会写入历史了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71E')

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_6C7',
    )

    ChrTalk(
        0x00FE,
        (
            '想不到情报部的那些家伙在\n',
            '背地里开发出了那样的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果队长没来的话\n',
            '王都会变得怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71E')

    def _loc_6C7(): pass

    label('loc_6C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_71E',
    )

    ChrTalk(
        0x00FE,
        (
            '尤莉亚上尉\n',
            '现在不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了给埃尔赛尤换引擎，\n',
            '她现在在雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_71E(): pass

    label('loc_71E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x722
@scena.Code('func_06_722')
def func_06_722():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_7B3',
    )

    ChrTalk(
        0x00FE,
        (
            '我们亲卫队如果不能用枪的话，\n',
            '作战能力就会下降了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这时候帝国来进攻的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎，\n',
            '对了，帝国也一样不能用枪啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_880')

    def _loc_7B3(): pass

    label('loc_7B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_81C',
    )

    ChrTalk(
        0x00FE,
        (
            '以前亲卫队好像\n',
            '有个很厉害的大队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是个被称为魔鬼\n',
            '大队长的人，\n',
            '到底是怎样一个人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_880')

    def _loc_81C(): pass

    label('loc_81C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_880',
    )

    ChrTalk(
        0x00FE,
        (
            '现在已经号称拥有最高性能的埃尔\n',
            '赛尤竟然还要更为进化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底要变成一艘怎样的船啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_880(): pass

    label('loc_880')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
