import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0012_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0012   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0012.x'
    header.mapIndex       = 232
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/E0012._SN', 'ED6_DT01/E0012_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            word_3A         = 232,
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
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT06/CH20078._CH', 'ED6_DT06/CH20078P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = -37000,
            z                   = -3800,
            y                   = 145500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '雷曼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '菲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '伊格尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '威尔姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 115320,
            z                   = 0,
            y                   = 100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 117500,
            z                   = 0,
            y                   = 100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1F8',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0B_F21)

    def _loc_1F8(): pass

    label('loc_1F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_206',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0C_151E)

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_218',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    def _loc_218(): pass

    label('loc_218')

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 58980, -2000, 54010, 5)
    ChrSetFlags(0x0009, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 28040, 0, -7450, 270)
    ChrClearFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_02_2E3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_271',
    )

    ChrSetPos(0x0008, 29550, 0, 8860, 90)

    Jump('loc_282')

    def _loc_271(): pass

    label('loc_271')

    ChrSetPos(0x0008, 32860, 0, 7250, 180)

    def _loc_282(): pass

    label('loc_282')

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 60760, -2000, 53780, 45)
    ChrSetFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 60590, 0, 3070, 265)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 88670, 0, -280, 81)

    Return()

# id: 0x0001 offset: 0x2CA
@scena.Code('func_01_2CA')
def func_01_2CA():
    OP_10(0x00, 0x00)
    PlaySE(122, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_2E2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2E2(): pass

    label('loc_2E2')

    Return()

# id: 0x0002 offset: 0x2E3
@scena.Code('func_02_2E3')
def func_02_2E3():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_308',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_44A')

    def _loc_308(): pass

    label('loc_308')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_321',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_44A')

    def _loc_321(): pass

    label('loc_321')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_44A')

    def _loc_33A(): pass

    label('loc_33A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_353',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_44A')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_44A')

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_385',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_44A')

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_44A')

    def _loc_39E(): pass

    label('loc_39E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_44A')

    def _loc_3B7(): pass

    label('loc_3B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D0',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_44A')

    def _loc_3D0(): pass

    label('loc_3D0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_44A')

    def _loc_3E9(): pass

    label('loc_3E9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_402',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_44A')

    def _loc_402(): pass

    label('loc_402')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41B',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_44A')

    def _loc_41B(): pass

    label('loc_41B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_434',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_44A')

    def _loc_434(): pass

    label('loc_434')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_45F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_44A')

    def _loc_45F(): pass

    label('loc_45F')

    Return()

# id: 0x0003 offset: 0x460
@scena.Code('func_03_460')
def func_03_460():
    SetScenaFlags(ScenaFlag(0x00B9, 4, 0x5CC))
    TalkBegin(0x00FE)
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000F,
        (
            '#0070090766V#061F#5P我说，阿加特大哥哥。\n',
            '让我看看你的战术导力器吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090767V用这个简易测量器，\n',
            '就可以看出哪里出问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050090768V#052F#6P啊啊，给你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090769V#051F我说你啊。\n',
            '一看到机械，眼神立刻就变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000F, 255)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x556
@scena.Code('func_04_556')
def func_04_556():
    SetScenaFlags(ScenaFlag(0x00B9, 4, 0x5CC))
    TalkBegin(0x00FE)
    OP_4A(0x000E, 255)

    ChrTalk(
        0x000F,
        (
            '#0070090766V#061F#5P我说，阿加特大哥哥。\n',
            '让我看看你的战术导力器吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090767V用这个简易测量器，\n',
            '就可以看出哪里出问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0050090768V#052F#6P啊啊，给你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090769V#051F我说你啊。\n',
            '一看到机械，眼神立刻就变了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000E, 255)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x64C
@scena.Code('func_05_64C')
def func_05_64C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_764',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6D3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560090675V#690F怎么了，\n',
            '你们就这么担心这个集装箱吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090676V#691F我会好好安排的，\n',
            '请放心地去休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_761')

    def _loc_6D3(): pass

    label('loc_6D3')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0560090677V#691F哦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090678V到雷斯顿要塞\n',
            '要３０分钟左右的航程。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090679V集装箱的伪装做好之前\n',
            '你们就先休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_761(): pass

    label('loc_761')

    Jump('loc_768')

    def _loc_764(): pass

    label('loc_764')

    Call(0, 0x000D)
    def _loc_768(): pass

    label('loc_768')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x76C
@scena.Code('func_06_76C')
def func_06_76C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_7A5',
    )

    ChrTalk(
        0x00FE,
        (
            '快要到了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是很紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AD')

    def _loc_7A5(): pass

    label('loc_7A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_83B',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '一想到博士被他们绑架了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我有点不寒而栗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为如果不请教博士的话，\n',
            '是不可能知道关于\n',
            '『卡佩尔』的详细情况的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AD')

    def _loc_83B(): pass

    label('loc_83B')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士\n',
            '竟然被绑架了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一直瞒着我们，\n',
            '工房长也太不够意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是认为\n',
            '我们不值得信任啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8AD(): pass

    label('loc_8AD')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x8B1
@scena.Code('func_07_8B1')
def func_07_8B1():
    TalkBegin(0x00FE)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵呀～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x8CB
@scena.Code('func_08_8CB')
def func_08_8CB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_911',
    )

    ChrTalk(
        0x00FE,
        (
            '就快能看见\n',
            '雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们一定要加把劲哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A80')

    def _loc_911(): pass

    label('loc_911')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_974',
    )

    ChrTurnDirection(0x00FE, 0x0009, 400)

    ChrTalk(
        0x00FE,
        (
            '喂，雷曼。\n',
            '赶快修正一下航线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从瓦雷利亚湖吹来的风\n',
            '把船尾吹得有些偏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A80')

    def _loc_974(): pass

    label('loc_974')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0009, 400)

    ChrTalk(
        0x00FE,
        (
            '喂，雷曼。\n',
            '往北北东方向偏离了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，真恼火！\n',
            '赶快修正一下航线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就在现在，\n',
            '说不定拉赛尔那家伙\n',
            '正遭受着危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '哎呀，真是的！\n',
            '伊格尔爷爷你就别说了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样一直抱怨着，\n',
            '我会分心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A80(): pass

    label('loc_A80')

    ChrSetDirection(0x00FE, 45, 400)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xA8B
@scena.Code('func_09_A8B')
def func_09_A8B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_ADF',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '谢谢你们\n',
            '特地给我送过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好、好了，\n',
            '现在必须集中精神工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

    def _loc_ADF(): pass

    label('loc_ADF')

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B09',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x035E)"),
            Expr.Return,
        ),
        'loc_B09',
    )

    Call(1, 0x0002)
    TalkEnd(0x00FE)

    Return()

    def _loc_B09(): pass

    label('loc_B09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C2C',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_B68',
    )

    ChrTalk(
        0x00FE,
        (
            '集装箱的伪装工作已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能和计划一样\n',
            '顺利进行就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C29')

    def _loc_B68(): pass

    label('loc_B68')

    ChrSetFlags(0x000A, 0x0010)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_BD0',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，菲！\n',
            '现在正是集中精力的时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把鲁迪和布拉姆都忘掉，\n',
            '赶快工作啊工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C24')

    def _loc_BD0(): pass

    label('loc_BD0')

    ChrTalk(
        0x00FE,
        (
            '好了，菲！\n',
            '现在正是集中精力的时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把个人的烦恼都忘掉，\n',
            '赶快工作啊工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C24(): pass

    label('loc_C24')

    ChrClearFlags(0x000A, 0x0010)

    def _loc_C29(): pass

    label('loc_C29')

    Jump('loc_D41')

    def _loc_C2C(): pass

    label('loc_C2C')

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_C87',
    )

    ChrTalk(
        0x00FE,
        (
            '集装箱的伪装工作已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能和计划一样\n',
            '顺利进行就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D41')

    def _loc_C87(): pass

    label('loc_C87')

    ChrTalk(
        0x00FE,
        (
            '没想到，拉赛尔博士\n',
            '竟然是被王国军绑架的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来\n',
            '我们的使命就太重大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是伪装的集装箱暴露了，\n',
            '不仅救出作战会失败，\n',
            '中央工房也会受到牵连。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要仔细再仔细啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D41(): pass

    label('loc_D41')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xD45
@scena.Code('func_0A_D45')
def func_0A_D45():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_DA1',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然是经常走的航路，\n',
            '不过今天还是相当紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可千万不要露出破绽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1D')

    def _loc_DA1(): pass

    label('loc_DA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E02',
    )

    ChrTalk(
        0x00FE,
        (
            '风的流向\n',
            '我早就知道啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我觉得\n',
            '比起风的流向，\n',
            '老爷子你才更让我担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1D')

    def _loc_E02(): pass

    label('loc_E02')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_4A(0x000B, 255)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0009, 400)

    ChrTalk(
        0x000B,
        (
            '喂，雷曼。\n',
            '往北北东方向偏离了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊啊，真恼火！\n',
            '赶快修正一下航线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就在现在，\n',
            '说不定拉赛尔那家伙\n',
            '正遭受着危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是的！\n',
            '伊格尔爷爷你就别说了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一直抱怨着，\n',
            '我会分心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 45, 400)
    OP_4B(0x000B, 255)

    def _loc_F1D(): pass

    label('loc_F1D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xF21
@scena.Code('func_0B_F21')
def func_0B_F21():
    MapClearFlags(0x02000000)
    EventBegin(0x00)
    CameraMove(29240, 0, 7250, 0)
    OP_67(0, 10730, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 28810, 0, 8640, 90)
    ChrSetPos(0x0101, 29240, 0, 7250, 90)
    ChrSetPos(0x0102, 28260, 0, 6830, 90)
    ChrSetPos(0x0106, 29420, 0, 6290, 45)
    ChrSetPos(0x0107, 28480, 0, 6070, 45)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0560090657V#691F这个就是给你们藏身的集装箱。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090658V藏四个人可能有点挤，\n',
            '不过就稍微忍耐一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090659V#501F#6P是这样吗？\n',
            '可是这个集装箱看起来很大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560090660V#693F哈哈～因为大部分要用来伪装，\n',
            '所以空的地方可是连一半都不到啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090661V啊哈哈……\n',
            '一起钻进去的话会很挤哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090662V#007F#6P原来是这样啊，那还真是狭小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090663V#010F没关系，只要姿势协调的话，\n',
            '用作藏身还是绰绰有余的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090664V#053F这就足够了。\n',
            '现在可不是讲究舒服的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0008, 400)

    ChrTalk(
        0x0106,
        (
            '#0050090665V#050F对了，大叔。\n',
            '有修理战术导力器的设备吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090666V我的导力器有点不好使，\n',
            '想趁现在调整一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1244')
    def lambda_1244():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1244)

    @scena.Lambda('lambda_1252')
    def lambda_1252():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1252)

    @scena.Lambda('lambda_1260')
    def lambda_1260():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1260)

    ChrTurnDirection(0x0008, 0x0106, 400)

    ChrTalk(
        0x0008,
        (
            '#0560090667V#691F啊，里面的工房设施里有，\n',
            '你们可以随时到那去整理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090668V#560F啊……\n',
            '我也一起去调整感应阻碍器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090669V阿加特大哥哥，请走这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)

    @scena.Lambda('lambda_1329')
    def lambda_1329():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_1329')

    DispatchAsync2(0x0106, 0x0001, lambda_1329)

    ChrTalk(
        0x0106,
        (
            '#0050090670V#052F啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_135B')
    def lambda_135B():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_135B')

    DispatchAsync2(0x0101, 0x0001, lambda_135B)

    @scena.Lambda('lambda_136C')
    def lambda_136C():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_136C')

    DispatchAsync2(0x0102, 0x0001, lambda_136C)

    ChrWalkTo(0x0107, 30080, 0, 3760, 3000, 0x00)

    @scena.Lambda('lambda_1391')
    def lambda_1391():
        ChrWalkTo(0x00FE, 29980, 0, -5870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1391)

    ChrWalkTo(0x0106, 29980, 0, 3480, 3000, 0x00)

    @scena.Lambda('lambda_13C0')
    def lambda_13C0():
        ChrWalkTo(0x00FE, 29980, 0, -5870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_13C0)

    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_13E8')
    def lambda_13E8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13E8)

    @scena.Lambda('lambda_13F6')
    def lambda_13F6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_13F6)

    ChrTalk(
        0x0008,
        (
            '#0560090671V#691F到雷斯顿要塞的航程\n',
            '大约需要３０分钟左右的时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090672V我也要将给集装箱做一下伪装工作，\n',
            '在那之前，你们先休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090673V#006F#6P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090674V#010F那就有劳维修长你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0106, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetPos(0x0106, 29240, 0, 7250, 0)
    ChrSetPos(0x0107, 29240, 0, 7250, 0)
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x00AC, 1, 0x561))
    EventEnd(0x00)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x06, 0xFF)

    Return()

# id: 0x000C offset: 0x151E
@scena.Code('func_0C_151E')
def func_0C_151E():
    EventBegin(0x00)
    FormationAddMember(0x05, 0xFF)
    FormationAddMember(0x06, 0xFF)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    CameraMove(116590, 0, 5710, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0106, 115790, 0, 4200, 0)
    ChrSetPos(0x0107, 115590, 0, 5610, 90)
    OP_89(0x0101, 113320, -2000, 7580, 0)
    OP_89(0x0102, 113320, -2000, 7580, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070090694V#061F#5P嘿咻～\n',
            '好了，这样就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090695V还好是小问题～～\n',
            '只是结晶链连接部分的齿轮松了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090696V#053F真是……\n',
            '老爱多管闲事的小鬼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090697V这种程度的修理，\n',
            '我自己也做得到嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090698V#051F不过，还是谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090699V#061F#5P嘿嘿……\n',
            '你太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090700V#063F啊，说起来……\n',
            '身体已经不要紧了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090701V有没有不舒服的感觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090702V#053F啊，没事了。\n',
            '根本用不着那么担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090703V#050F与其花时间担心别人，\n',
            '还不如先为自己打算一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090704V到现在还没有回去的念头吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090705V#065F#5P我、我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090706V#552F不要误会了。\n',
            '既然你决定了，我也不想再说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090707V只是……你不觉得害怕吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090708V#064F#5P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090709V#050F虽说这是为了救爷爷，\n',
            '但我们可是要私闯军事设施啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090710V要知道你只是个小鬼，\n',
            '还没到承受这么大的重担的年纪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090711V为什么能这样满不在乎地跟来？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090712V#562F#5P这、这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090713V说实话，我真的很害怕……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090714V#560F但是但是，\n',
            '有艾丝蒂尔姐姐和约修亚哥哥在……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090715V而且还有阿加特大哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090716V这样我就觉得安心大于害怕了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090717V#067F嘿嘿……\n',
            '可能是我有点迟钝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090718V#052F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090719V#051F呵呵。\n',
            '不是有点，是相当迟钝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090720V看来担心你也是多余的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090721V#067F#5P嘿嘿……不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090722V#060F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090723V#560F那、那个……\n',
            '有件事我可以问问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090724V#052F什么事，突然这么问？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090725V#060F#5P嗯，那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090726V米夏，是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050090727V#057F你怎么知道这个名字？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090728V#065F#5P那、那个那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090729V阿加特大哥哥昨晚昏迷的时候\n',
            '是这样叫我的呢……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090730V#063F……对不起，\n',
            '是不能问的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090731V#053F不……\n',
            '也没什么好隐瞒的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090732V#050F米夏……是我的妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090733V#064F#5P哇，阿加特是哥哥啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090734V#061F那么你妹妹有多大呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090735V应该比我大吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090736V#552F唔……这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090737V#051F我想应该和你的年纪差不多吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090738V#064F#5P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090739V嗯……\n',
            '你不常和妹妹见面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090740V#051F啊，因为我这职业的关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090741V只有每年回乡的时候才能见她一次。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090742V#063F#5P是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090743V……米夏她，\n',
            '真是有点可怜呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090744V#055F怎、怎么了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090745V#067F#5P因为……我要是也有个\n',
            '像阿加特大哥哥这样的哥哥，\n',
            '我一定会想经常和他在一起的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090746V#062F总、总之……\n',
            '我有点同情米夏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090747V#055F是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090748V#552F不过，的确也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090749V要是我那时能像这样强的话，\n',
            '也许大家就能一直在一起了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090750V#064F#5P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(166, 0x00, 0x64)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('乘务员的声音')

    Talk(
        (
            '#2700090751V',
            (TxtCtl.SetColor, 0x5),
            '本飞艇马上\n',
            '就要到达雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2700090752V',
            (TxtCtl.SetColor, 0x5),
            '请各位游击士\n',
            '尽快到货舱集合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0106,
        (
            '#0050090753V#052F哦，差不多是时候了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_212A')
    def lambda_212A():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_212A')

    DispatchAsync2(0x0101, 0x0001, lambda_212A)

    @scena.Lambda('lambda_213B')
    def lambda_213B():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_213B')

    DispatchAsync2(0x0102, 0x0001, lambda_213B)

    @scena.Lambda('lambda_214C')
    def lambda_214C():
        CameraMove(114220, 0, 4820, 1500)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_214C)

    @scena.Lambda('lambda_2164')
    def lambda_2164():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2164)

    @scena.Lambda('lambda_2176')
    def lambda_2176():
        ChrWalkTo(0x00FE, 113480, 0, 3470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2176)

    @scena.Lambda('lambda_2191')
    def lambda_2191():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2191)

    ChrWalkTo(0x0102, 112690, 0, 4260, 2000, 0x00)

    @scena.Lambda('lambda_21B7')
    def lambda_21B7():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_21B7)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090754V#501F啊，找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21EF')
    def lambda_21EF():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_21EF)

    @scena.Lambda('lambda_21FD')
    def lambda_21FD():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_21FD)

    @scena.Lambda('lambda_220B')
    def lambda_220B():
        ChrWalkTo(0x00FE, 114670, 0, 3370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_220B)

    @scena.Lambda('lambda_2226')
    def lambda_2226():
        ChrWalkTo(0x00FE, 113920, 0, 3900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2226)

    @scena.Lambda('lambda_2241')
    def lambda_2241():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_2241')

    DispatchAsync2(0x0102, 0x0001, lambda_2241)

    CameraMove(116590, 0, 5710, 1500)

    ChrTalk(
        0x0107,
        (
            '#0070090755V#560F#5P啊，姐姐你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090756V#006F你们也听到广播了吧。\n',
            '飞艇差不多要到要塞了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090757V#010F准备好了就一起去货舱吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090758V#053F#2P好，准备完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090759V#000F提妲呢，\n',
            '那个装置的情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090760V#060F#5P嗯，很好。\n',
            '时机也测试过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090761V如果没有意外的话,\n',
            '一定可以瞒过生命感应器的监测。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090762V#006F太好了！\n',
            '真是令人心安的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090763V#010F全靠你了，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090764V#061F#5P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090765V#051F#2P好了。\n',
            '那么我们快去货舱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_21()

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1E()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetScenaFlags(ScenaFlag(0x00AC, 2, 0x562))
    OP_28(0x0044, 0x01, 0x0001)
    MapSetFlags(0x02000000)
    MapSetFlags(0x00000800)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x24A8
@scena.Code('func_0D_24A8')
def func_0D_24A8():
    EventBegin(0x00)
    MapClearFlags(0x00000800)
    Fade(1000)
    CameraMove(33030, 0, 6430, 0)
    OP_67(0, 9490, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 32860, 0, 7250, 180)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0106, 0x0004)
    ChrSetFlags(0x0107, 0x0004)
    ChrSetPos(0x0102, 32450, 0, 5900, 0)
    ChrSetPos(0x0101, 33410, 0, 5850, 0)
    ChrSetPos(0x0106, 32200, 0, 4810, 0)
    ChrSetPos(0x0107, 33070, 0, 4590, 0)

    @scena.Lambda('lambda_256A')
    def lambda_256A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_256A')

    DispatchAsync2(0x0102, 0x0002, lambda_256A)

    @scena.Lambda('lambda_257B')
    def lambda_257B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_257B')

    DispatchAsync2(0x0101, 0x0002, lambda_257B)

    @scena.Lambda('lambda_258C')
    def lambda_258C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_258C')

    DispatchAsync2(0x0107, 0x0002, lambda_258C)

    @scena.Lambda('lambda_259D')
    def lambda_259D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_259D')

    DispatchAsync2(0x0106, 0x0002, lambda_259D)

    OP_4A(0x0008, 255)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0560090770V#691F哦哦，来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090771V#006F准备已经完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560090772V#691F集装箱的伪装工作已经做好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2634')
    def lambda_2634():
        CameraMove(31660, 0, 8900, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2634)

    ChrWalkTo(0x0008, 32549, 0, 7070, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    PlaySE(168, 0x00, 0x64)
    OP_70(0x0003, 180)
    OP_73(0x0003)

    ChrTalk(
        0x0008,
        (
            '#0560090773V#691F即使他们打开普通盖子，\n',
            '也只能看到维修船壳用的金属板……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 32570, 0, 8950, 2000, 0x00)
    PlaySE(169, 0x00, 0x64)
    OP_70(0x0004, 180)
    OP_73(0x0004)

    ChrTalk(
        0x0008,
        (
            '#0560090774V#693F这边还有个暗门。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2719')
    def lambda_2719():
        CameraMove(33030, 0, 6430, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2719)

    ChrWalkTo(0x0008, 33470, 0, 7160, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010090775V#004F嘿嘿～很巧妙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090776V#010F接下来只要使生命感应器无效化，\n',
            '应该就能顺利潜入了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560090777V#690F好了。\n',
            '接下来你们就藏进去吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090778V准备好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090779V#006F当然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090780V#051F随时ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560090781V#691F好！\n',
            '那么挨个儿进去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090782V大家藏好后我就把暗门关上。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090783V#010F明白了。\n',
            '那么就由我第一个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_28E0')
    def lambda_28E0():
        CameraMove(31660, 0, 8900, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28E0)

    @scena.Lambda('lambda_28F8')
    def lambda_28F8():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_28F8')

    DispatchAsync2(0x0101, 0x0002, lambda_28F8)

    @scena.Lambda('lambda_2909')
    def lambda_2909():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2909')

    DispatchAsync2(0x0107, 0x0002, lambda_2909)

    @scena.Lambda('lambda_291A')
    def lambda_291A():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_291A')

    DispatchAsync2(0x0106, 0x0002, lambda_291A)

    @scena.Lambda('lambda_292B')
    def lambda_292B():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_292B')

    DispatchAsync2(0x0008, 0x0002, lambda_292B)

    ChrWalkTo(0x0102, 32689, 0, 7180, 2000, 0x00)
    ChrWalkTo(0x0102, 32549, 0, 9150, 2000, 0x00)
    ChrWalkTo(0x0102, 31110, 0, 9150, 1000, 0x00)
    ChrWalkTo(0x0101, 32689, 0, 7180, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090784V#007F果然是太狭小了，\n',
            '不得不紧紧地靠在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090785V#503F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29F3')
    def lambda_29F3():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_29F3')

    DispatchAsync2(0x0107, 0x0002, lambda_29F3)

    @scena.Lambda('lambda_2A04')
    def lambda_2A04():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2A04')

    DispatchAsync2(0x0106, 0x0002, lambda_2A04)

    @scena.Lambda('lambda_2A15')
    def lambda_2A15():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2A15')

    DispatchAsync2(0x0008, 0x0002, lambda_2A15)

    ChrTalk(
        0x0102,
        (
            '#0020090786V#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090787V艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090788V#504F没、没什么啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A88')
    def lambda_2A88():
        CameraSetDistance(2300, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A88)

    @scena.Lambda('lambda_2A98')
    def lambda_2A98():
        CameraMove(31110, 0, 9150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2A98)

    ChrWalkTo(0x0101, 32549, 0, 9150, 2000, 0x00)
    ChrWalkTo(0x0101, 31110, 0, 9150, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010090789V#505F#2P嘿哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090790V#015F#1P艾丝蒂尔，\n',
            '麻烦你的头向那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090791V#006F#2PＯＫ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090792V#004F………………啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090793V#503F我、我说约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090794V这个姿势，你能不能换一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090795V#018F#1P忍、忍耐一下嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090796V不这样的话，\n',
            '没办法让四个人都挤进来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090797V#503F#2P是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090798V是啊，没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090799V#015F#1P咳咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090800V#010F下一个是提妲，\n',
            '最后是阿加特兄。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090801V这样四个人应该都能进来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090802V#061F#1P嗯。\n',
            '那我进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2D10')
    def lambda_2D10():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_2D10')

    DispatchAsync2(0x0106, 0x0002, lambda_2D10)

    @scena.Lambda('lambda_2D21')
    def lambda_2D21():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_2D21')

    DispatchAsync2(0x0008, 0x0002, lambda_2D21)

    ChrWalkTo(0x0107, 32689, 0, 7180, 2000, 0x00)
    ChrWalkTo(0x0107, 32549, 0, 9150, 2000, 0x00)
    ChrWalkTo(0x0107, 31110, 0, 9150, 1000, 0x00)

    ChrTalk(
        0x0107,
        (
            '#0070090803V#062F#2P嘿咻……\n',
            '姐姐，对不起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090804V#001F#1P哇，提妲。\n',
            '暖暖的又好～软哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090805V嗯……\n',
            '还有好像牛奶一样的香味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090806V#065F#2P姐、姐姐……\n',
            '不要抱得人家那么紧嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090807V有点辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090808V#507F#1P呵呵呵……\n',
            '好啦，抱一下也没关系嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090809V#502F嗯……\n',
            '这小脸蛋的手感可真是好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090810V#067F#2P啊嗯～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090811V#018F#3P艾丝蒂尔……别闹啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0106, 32689, 0, 7180, 2000, 0x00)

    ChrTalk(
        0x0106,
        (
            '#0050090812V#551F哎呀哎呀……\n',
            '我有种无端的不安啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090813V#054F喂喂。\n',
            '你们就不能多让点地方给我吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F9F')
    def lambda_2F9F():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_2F9F')

    DispatchAsync2(0x0008, 0x0002, lambda_2F9F)

    ChrWalkTo(0x0106, 32549, 0, 9150, 2000, 0x00)
    ChrWalkTo(0x0106, 31110, 0, 9150, 1000, 0x00)

    ChrTalk(
        0x0107,
        (
            '#0070090814V#065F#1P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090815V#052F#2P哎呀……很挤吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090816V#560F#1P不，没事。\n',
            '没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090817V我能忍耐的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090818V#050F#2P不要勉强啊，\n',
            '觉得挤直接说就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090819V#067F#1P啊，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090820V#051F#2P好了，大叔。\n',
            '这里的准备完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560090821V#691F知道了。\n',
            '我这就要关上暗门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrWalkTo(0x0008, 32570, 0, 8950, 2000, 0x00)
    Sleep(500)

    @scena.Lambda('lambda_3156')
    def lambda_3156():
        CameraSetDistance(2600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3156)

    PlaySE(169, 0x00, 0x64)
    OP_6F(0x0004, 180)
    OP_70(0x0004, 0)
    OP_73(0x0004)

    ChrTalk(
        0x0008,
        (
            '#0560090822V#691F着陆之后马上就会把集装箱搬出来。\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090823V那时可能有点晃，\n',
            '你们要稍微忍耐一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 32549, 0, 7070, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(500)

    OP_6F(0x0003, 180)
    OP_70(0x0003, 0)
    Sleep(600)

    PlaySE(168, 0x00, 0x64)
    OP_73(0x0003)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C3102._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
