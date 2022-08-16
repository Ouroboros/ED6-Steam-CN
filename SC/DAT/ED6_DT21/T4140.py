import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4140_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4140   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4140.x'
    header.mapIndex       = 1
    header.bgm            = 34
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
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '夏伊',
            x                   = 1260,
            z                   = 0,
            y                   = -240,
            direction           = 236,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '史帕德',
            x                   = -500,
            z                   = 0,
            y                   = 129840,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '塞森',
            x                   = 58580,
            z                   = 0,
            y                   = 360,
            direction           = 102,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '多姆',
            x                   = 120030,
            z                   = 0,
            y                   = -1260,
            direction           = 10,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -10,
            triggerZ            = 0,
            triggerY            = -1600,
            triggerRange        = 800,
            actorX              = 1260,
            actorZ              = 1500,
            actorY              = -240,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60410,
            triggerZ            = 0,
            triggerY            = 390,
            triggerRange        = 800,
            actorX              = 58580,
            actorZ              = 1500,
            actorY              = 360,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 119960,
            triggerZ            = 0,
            triggerY            = 650,
            triggerRange        = 800,
            actorX              = 120030,
            actorZ              = 1500,
            actorY              = -1260,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1BE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F3',
    )

    TerminateThread(0x000B, 0x00)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, 125240, 200, -1310, 90)

    def _loc_1F3(): pass

    label('loc_1F3')

    Return()

# id: 0x0001 offset: 0x1F4
@scena.Code('func_01_1F4')
def func_01_1F4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_205',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_205(): pass

    label('loc_205')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_215',
    )

    OP_64(0x02, 0x0001)

    def _loc_215(): pass

    label('loc_215')

    Return()

# id: 0x0002 offset: 0x216
@scena.Code('func_02_216')
def func_02_216():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_239',
    )

    OP_8D(0x0009, 1470, 131290, -1690, 128210, 2000)

    Jump('func_02_216')

    def _loc_239(): pass

    label('loc_239')

    Return()

# id: 0x0003 offset: 0x23A
@scena.Code('func_03_23A')
def func_03_23A():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x23F
@scena.Code('func_04_23F')
def func_04_23F():
    TalkBegin(0x000A)
    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_259',
    )

    OP_A9(0xC8)
    TalkEnd(0x000A)

    Return()

    def _loc_259(): pass

    label('loc_259')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26A',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_26A(): pass

    label('loc_26A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_2BE',
    )

    ChrTalk(
        0x000A,
        (
            '这是怎么了？\n',
            '这么惊惶失措的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们的店可不会逃避。\n',
            '好好看着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_311')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_311',
    )

    ChrTalk(
        0x000A,
        (
            '最近在晚上\n',
            '南街区的店也在营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '也是，只要能赚钱，\n',
            '多辛苦都正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_311(): pass

    label('loc_311')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x315
@scena.Code('func_05_315')
def func_05_315():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x31A
@scena.Code('func_06_31A')
def func_06_31A():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_345',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_33F',
    )

    OP_A9(0xDA)

    Jump('loc_341')

    def _loc_33F(): pass

    label('loc_33F')

    OP_A9(0xC9)

    def _loc_341(): pass

    label('loc_341')

    TalkEnd(0x0008)

    Return()

    def _loc_345(): pass

    label('loc_345')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_356',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_356(): pass

    label('loc_356')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_3C0',
    )

    ChrTalk(
        0x0008,
        (
            '哼，受不了了。\n',
            '还是要离家出走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊……对、对不起。\n',
            '欢迎！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46C')

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_46C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44B',
    )

    ChrTalk(
        0x0008,
        (
            '哈……\n',
            '我和丈夫大吵了一架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然这么说，不过他根本就不说话，\n',
            '都是我一个人在上窜下跳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '感觉好空虚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_46C')

    def _loc_44B(): pass

    label('loc_44B')

    ChrTalk(
        0x0008,
        (
            '对他来说\n',
            '我根本就不重要……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46C(): pass

    label('loc_46C')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x470
@scena.Code('func_07_470')
def func_07_470():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x475
@scena.Code('func_08_475')
def func_08_475():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_4C3',
    )

    ChrTalk(
        0x000B,
        (
            '可能是因为夜晚的\n',
            '黑暗，可以集中精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好，加油修理吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_517')

    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_517',
    )

    ChrTalk(
        0x000B,
        (
            '呼，这可难办了……\n',
            '结晶回路好像短路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '把这儿这么弄一下……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_517(): pass

    label('loc_517')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x51B
@scena.Code('func_09_51B')
def func_09_51B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_58D',
    )

    ChrTalk(
        0x00FE,
        (
            '和妻子吵架了，\n',
            '她没给我做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法我只能做了\n',
            '意大利面来吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可这更加\n',
            '激怒了她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64F')

    def _loc_58D(): pass

    label('loc_58D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_64F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_613',
    )

    ChrTalk(
        0x00FE,
        (
            '关于店里的事，\n',
            '我想和妻子谈谈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可因为一点小事\n',
            '激怒了她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就默不作声，\n',
            '所以她以为我不想谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_64F')

    def _loc_613(): pass

    label('loc_613')

    ChrTalk(
        0x00FE,
        (
            '我绝不是\n',
            '不关心妻子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可我不知道\n',
            '该说什么好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64F(): pass

    label('loc_64F')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
