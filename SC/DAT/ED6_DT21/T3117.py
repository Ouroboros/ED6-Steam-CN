import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3117_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3117   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3117.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0001
    header.entryFunction  = 0x0000
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3117_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雷伊',
            x                   = 1070,
            z                   = 0,
            y                   = 9970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '蒂亚利',
            x                   = -3500,
            z                   = 0,
            y                   = 14150,
            direction           = 0,
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
            name                = '米优',
            x                   = -2590,
            z                   = 0,
            y                   = 8420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '安东尼',
            x                   = 3650,
            z                   = 0,
            y                   = 2680,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -5350,
            triggerZ            = 0,
            triggerY            = 4760,
            triggerRange        = 1000,
            actorX              = -5350,
            actorZ              = 500,
            actorY              = 4760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0001,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5500,
            triggerZ            = 0,
            triggerY            = 5390,
            triggerRange        = 1000,
            actorX              = 5500,
            actorZ              = 500,
            actorY              = 5390,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4470,
            triggerZ            = 1000,
            triggerY            = 14290,
            triggerRange        = 1000,
            actorX              = 4470,
            actorZ              = 1500,
            actorY              = 14290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1750,
            triggerZ            = 0,
            triggerY            = 12760,
            triggerRange        = 1000,
            actorX              = 1750,
            actorZ              = 0,
            actorY              = 12760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_204',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1EB',
    )

    Jump('loc_201')

    def _loc_1EB(): pass

    label('loc_1EB')

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, 4490, 1000, 8220, 0)

    def _loc_201(): pass

    label('loc_201')

    Jump('loc_286')

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_224',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -2590, 0, 9570, 270)

    Jump('loc_286')

    def _loc_224(): pass

    label('loc_224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_24E',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -2590, 0, 9570, 180)
    ChrSetFlags(0x0009, 0x0010)
    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_286')

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_27A',
    )

    ChrSetPos(0x0008, 5290, 1000, 8740, 0)
    ChrSetPos(0x0009, -2590, 0, 9570, 270)

    Jump('loc_286')

    def _loc_27A(): pass

    label('loc_27A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_286',
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_286(): pass

    label('loc_286')

    Return()

# id: 0x0001 offset: 0x287
@scena.Code('func_01_287')
def func_01_287():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A6',
    )

    OP_79(0xFF, 0x0002)
    OP_7A(0x08, 0x0002)
    OP_7B()
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)

    def _loc_2A6(): pass

    label('loc_2A6')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)

    Return()

# id: 0x0002 offset: 0x2B7
@scena.Code('func_02_2B7')
def func_02_2B7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DA',
    )

    OP_8D(0x00FE, 4670, 5810, -4590, 550, 1000)

    Jump('func_02_2B7')

    def _loc_2DA(): pass

    label('loc_2DA')

    Return()

# id: 0x0003 offset: 0x2DB
@scena.Code('func_03_2DB')
def func_03_2DB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_3DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，终于来到\n',
            '这里了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力虽然停止了，\n',
            '不过温室总算没什么大碍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蒂亚利也完成了\n',
            '最低限度的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，也希望『埃尔赛尤』\n',
            '那边也能一切顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_3DE')

    def _loc_39A(): pass

    label('loc_39A')

    ChrTalk(
        0x00FE,
        (
            '温室也没事，\n',
            '暂时可以安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之要准备\n',
            '重新开始实验了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DE(): pass

    label('loc_3DE')

    Jump('loc_7B2')

    def _loc_3E1(): pass

    label('loc_3E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_5E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_47D',
    )

    ChrTalk(
        0x00FE,
        (
            '我也想要像一个提妲一样\n',
            '天真可爱的助手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，等温室的实验结束以后要\n',
            '开始进行导力人偶的开发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，模特儿\n',
            '当然是提妲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5DF')

    def _loc_47D(): pass

    label('loc_47D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BA',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们今天看上去也很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50F')

    def _loc_4BA(): pass

    label('loc_4BA')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0107, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哟，那不是\n',
            '提妲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们今天看上去也很忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50F(): pass

    label('loc_50F')

    ChrTalk(
        0x0107,
        (
            '#560F啊，是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我又来帮\n',
            '爷爷了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，拉赛尔博士\n',
            '真是有个好助手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相比之下，\n',
            '我现在的助手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '……算了，不耍嘴皮子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '提妲，不好意思。\n',
            '你回去工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F那我先过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5DF(): pass

    label('loc_5DF')

    Jump('loc_7B2')

    def _loc_5E2(): pass

    label('loc_5E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_6D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_643',
    )

    ChrTalk(
        0x00FE,
        (
            '世界上有很多\n',
            '可以研究的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是值得研究的东西\n',
            '却只有很少的一点点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D4')

    def _loc_643(): pass

    label('loc_643')

    ChrTalk(
        0x00FE,
        (
            '农作物的品种改良\n',
            '刚刚取得了前期的成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过培育一般的\n',
            '农作物并不有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，呆在研究室\n',
            '也找不到灵感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要去\n',
            '散个步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_6D4(): pass

    label('loc_6D4')

    Jump('loc_7B2')

    def _loc_6D7(): pass

    label('loc_6D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_7B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_732',
    )

    ChrTalk(
        0x00FE,
        (
            '蒂亚利还没决定\n',
            '本期的课题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，只能先把他\n',
            '当作助手使唤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7B2')

    def _loc_732(): pass

    label('loc_732')

    ChrTalk(
        0x00FE,
        (
            '呼，这次的课题\n',
            '仍然是温室的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然如此，不过是\n',
            '让蒂亚利一个人在做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，有什么可以有效\n',
            '利用温室的建议吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_7B2(): pass

    label('loc_7B2')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x7B6
@scena.Code('func_04_7B6')
def func_04_7B6():
    TalkBegin(0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x002A, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_7C6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_7C6(): pass

    label('loc_7C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_846',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇在上半部完成过QST042】\n'),
            TXT(0x01, '【◇在上半部没完成过QST042】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_83A'),
        (0x00000001, 'loc_840'),
        (-1, 'loc_846'),
    )

    def _loc_83A(): pass

    label('loc_83A')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_846')

    def _loc_840(): pass

    label('loc_840')

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_846')

    def _loc_846(): pass

    label('loc_846')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_993',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_938',
    )

    ChrTalk(
        0x00FE,
        (
            '雷伊前辈\n',
            '终于回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他之前好像和拉赛尔博士\n',
            '一起在『埃尔赛尤』上做研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在、在我管理温室的时候前辈\n',
            '已经在做这么尖端的研究了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可、可恶……！！\n',
            '我也不会输的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次的研究\n',
            '一定要拿出成果来！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_990')

    def _loc_938(): pass

    label('loc_938')

    ChrTalk(
        0x00FE,
        (
            '总觉得跟前辈的\n',
            '差距越来越大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我下次一定要努力\n',
            '嗯，导力枪的调整ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_990(): pass

    label('loc_990')

    Jump('loc_14CA')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 2, 0x20D2)),
            Expr.Return,
        ),
        'loc_A21',
    )

    ChrTalk(
        0x00FE,
        (
            '总、总之希望雷伊\n',
            '前辈能平安返回。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为导力器不工作了，\n',
            '所以温室管理也变得困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，前辈！\n',
            '请马上回来吧！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D4D')

    def _loc_A21(): pass

    label('loc_A21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CC0',
    )

    ChrTalk(
        0x00FE,
        (
            '雷、雷伊前辈不知道被\n',
            '带去哪儿了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以没办法，\n',
            '只能让我来做温室的管理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过因为导力器不工作了，\n',
            '所以温室管理也变得困难了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总、总之希望前辈\n',
            '早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 7, 0x20AF)),
            Expr.Return,
        ),
        'loc_CBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 0, 0x20B0)),
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BC1',
    )

    ChrTalk(
        0x0107,
        (
            '#064F那个，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们好像在古罗尼山顶\n',
            '看见过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '古、古罗尼山顶？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要不了多久\n',
            '应该会回来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '这，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正不管怎样只要\n',
            '他平安回来就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB7')

    def _loc_BC1(): pass

    label('loc_BC1')

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，先告诉你一下吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那位雷伊先生，\n',
            '我们在古罗尼山顶看见了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '古、古罗尼山顶？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，现在只能\n',
            '步行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然可能很花时间，\n',
            '不过他一定会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '这，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正不管怎样只要\n',
            '他平安回来就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB7(): pass

    label('loc_CB7')

    SetScenaFlags(ScenaFlag(0x041A, 2, 0x20D2))

    def _loc_CBA(): pass

    label('loc_CBA')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_D4D')

    def _loc_CC0(): pass

    label('loc_CC0')

    ChrTalk(
        0x00FE,
        (
            '雷伊前辈被带走了，\n',
            '只能让我来做温室的管理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过因为导力器不工作了，\n',
            '所以温室管理也变得困难了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，前辈！\n',
            '请快点回来！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D4D(): pass

    label('loc_D4D')

    Jump('loc_14CA')

    def _loc_D50(): pass

    label('loc_D50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 5, 0x142D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_10B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_106A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_E91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_DF8',
    )

    ChrTalk(
        0x00FE,
        (
            '课题啊……\n',
            '选什么好呢…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，米优小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……咦，我说\n',
            '我在想什么啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E8E')

    def _loc_DF8(): pass

    label('loc_DF8')

    ChrTalk(
        0x00FE,
        (
            '刚才新人来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有种未经世故的可爱啊～\n',
            '是个坦率活泼的女孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不，没时间\n',
            '想这些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，得早点决定\n',
            '研究课题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_E8E(): pass

    label('loc_E8E')

    Jump('loc_1067')

    def _loc_E91(): pass

    label('loc_E91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_F24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_EEE',
    )

    ChrTalk(
        0x00FE,
        (
            '那个，现在还处在\n',
            '寻找课题的阶段哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在决定之前我先\n',
            '帮前辈做实验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F21')

    def _loc_EEE(): pass

    label('loc_EEE')

    ChrTalk(
        0x00FE,
        (
            '嘿、嘿～你就是新人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很、很年轻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F21(): pass

    label('loc_F21')

    Jump('loc_1067')

    def _loc_F24(): pass

    label('loc_F24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1004',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F8F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，得早点决定下一个\n',
            '研究课题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好、好像我要被选为\n',
            '雷伊前辈的助手了，真可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1001')

    def _loc_F8F(): pass

    label('loc_F8F')

    ChrTalk(
        0x00FE,
        (
            '嗯，下一个课题\n',
            '选什么好呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总不能永远给雷伊\n',
            '前辈做帮手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再磨磨蹭蹭的话\n',
            '真的要被选为助手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1001(): pass

    label('loc_1001')

    Jump('loc_1067')

    def _loc_1004(): pass

    label('loc_1004')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1067',
    )

    ChrTalk(
        0x00FE,
        (
            '因为这里是４层，\n',
            '所以摇晃地比较厉害一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之地震没有造成\n',
            '设备的损坏真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1067(): pass

    label('loc_1067')

    Jump('loc_10B6')

    def _loc_106A(): pass

    label('loc_106A')

    ChrTalk(
        0x00FE,
        (
            '现在我正在\n',
            '寻找下一个课题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果再有什么事的话\n',
            '我还会联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_10B6(): pass

    label('loc_10B6')

    Jump('loc_14CA')

    def _loc_10B9(): pass

    label('loc_10B9')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见。\n',
            '还记得我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '瞧，我是蒂亚利啊。\n',
            '做过运动鞋研究的那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F哈哈，放心好了。\n',
            '我没忘记你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你是为斯托雷加社工作的吧。\n',
            '我怎么会忘了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F那蒂亚利先生你\n',
            '还在做鞋的研究？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，托你们的福\n',
            '研究目的已经达到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把数据送到斯托雷加社\n',
            '之后那个工作就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '……对了，按照约定我把你的\n',
            '口信也传达过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是『我期待着你们的新产品哦』那句，\n',
            '我就说是游击士中的爱好者说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F真、真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，当然是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '斯托雷加的开发者也\n',
            '非常激动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还开玩笑说\n',
            '『下次做游击士用的吧！』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F啊～是玩笑吗～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，那我就不知道了。\n',
            '只不过我觉得是玩笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正因此我的\n',
            '研究经费也增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我正在\n',
            '寻找下一个课题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次可能也会\n',
            '拜托协会帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到时候也麻烦\n',
            '你们一如既往地帮我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，你就\n',
            '不用客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F还有，我想不用\n',
            '我说你也知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1005F#3S斯托雷加社的委托\n',
            '我会放在第一位的！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哈、哈哈，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0285, 5, 0x142D))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    def _loc_14CA(): pass

    label('loc_14CA')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x14CE
@scena.Code('func_05_14CE')
def func_05_14CE():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_156E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_151F',
    )

    ChrTalk(
        0x00FE,
        (
            '老师您在做\n',
            '什么样的研究呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米优可能会很有兴趣的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156E')

    def _loc_151F(): pass

    label('loc_151F')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，初次见面～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是实习生\n',
            '米优～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能不能让我\n',
            '找找资料啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_156E(): pass

    label('loc_156E')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x1572
@scena.Code('func_06_1572')
def func_06_1572():
    TalkBegin(0x000B)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
