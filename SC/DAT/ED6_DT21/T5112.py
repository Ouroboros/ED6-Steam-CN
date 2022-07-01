import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5112_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5112   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '罗伯特'),
    TXT(0x02, '折断的枪'),
    TXT(0x03, '小说'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5112.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x21A4
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
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT26/CH20267._CH', 'ED6_DT26/CH20267P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 26690,
            z                   = 0,
            y                   = 5140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 18860,
            z                   = -300,
            y                   = 5310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 140520,
            z                   = 650,
            y                   = -33440,
            direction           = 85,
            word_0E             = 0,
            dword_10            = 1703938,
            chipIndex           = 2,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 25470,
            triggerZ            = -300,
            triggerY            = 4940,
            triggerRange        = 800,
            actorX              = 26690,
            actorZ              = 1500,
            actorY              = 5140,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18860,
            triggerZ            = -300,
            triggerY            = 5310,
            triggerRange        = 800,
            actorX              = 18860,
            actorZ              = -300,
            actorY              = 5310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 21170,
            triggerZ            = 0,
            triggerY            = 17380,
            triggerRange        = 800,
            actorX              = 20960,
            actorZ              = 1000,
            actorY              = 18200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 26900,
            triggerZ            = 0,
            triggerY            = 7220,
            triggerRange        = 800,
            actorX              = 28160,
            actorZ              = 1000,
            actorY              = 7060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 19970,
            triggerZ            = -300,
            triggerY            = 5580,
            triggerRange        = 800,
            actorX              = 19970,
            actorZ              = -300,
            actorY              = 5580,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 26550,
            triggerZ            = 110,
            triggerY            = 15520,
            triggerRange        = 800,
            actorX              = 27430,
            actorZ              = 1110,
            actorY              = 16059,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14070,
            triggerZ            = 0,
            triggerY            = 17590,
            triggerRange        = 800,
            actorX              = 14070,
            actorZ              = 1000,
            actorY              = 17590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 85780,
            triggerZ            = 0,
            triggerY            = 41480,
            triggerRange        = 700,
            actorX              = 85180,
            actorZ              = 500,
            actorY              = 41480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 113640,
            triggerZ            = 0,
            triggerY            = 41480,
            triggerRange        = 700,
            actorX              = 113040,
            actorZ              = 500,
            actorY              = 41480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 140520,
            triggerZ            = 0,
            triggerY            = -33440,
            triggerRange        = 800,
            actorX              = 140520,
            actorZ              = 1000,
            actorY              = -33440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x28A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29F',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_64(0x00, 0x0001)

    def _loc_29F(): pass

    label('loc_29F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 4, 0x101C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2AF',
    )

    Event(0, 0x0005)

    def _loc_2AF(): pass

    label('loc_2AF')

    Return()

# id: 0x0001 offset: 0x2B0
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D2',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 0)
    OP_64(0x00, 0x0001)

    Jump('loc_302')

    def _loc_2D2(): pass

    label('loc_2D2')

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_65(0x00, 0x0001)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 0)

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0216, 5, 0x10B5)),
            Expr.Return,
        ),
        'loc_312',
    )

    SetChrFlags(0x000A, 0x0080)
    OP_64(0x09, 0x0001)

    def _loc_312(): pass

    label('loc_312')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 3, 0x101B)),
            Expr.Return,
        ),
        'loc_327',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_327(): pass

    label('loc_327')

    Return()

# id: 0x0002 offset: 0x328
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_359'),
        (0x00000001, 'loc_365'),
        (0x00000002, 'loc_371'),
        (0x00000003, 'loc_37D'),
        (0x00000004, 'loc_389'),
        (0x00000005, 'loc_395'),
        (0x00000006, 'loc_3A1'),
        (-1, 'loc_3AD'),
    )

    def _loc_359(): pass

    label('loc_359')

    OP_99(0x00FE, 0x00, 0x07, 0x000005AA)

    Jump('loc_3B9')

    def _loc_365(): pass

    label('loc_365')

    OP_99(0x00FE, 0x00, 0x07, 0x0000060E)

    Jump('loc_3B9')

    def _loc_371(): pass

    label('loc_371')

    OP_99(0x00FE, 0x00, 0x07, 0x00000640)

    Jump('loc_3B9')

    def _loc_37D(): pass

    label('loc_37D')

    OP_99(0x00FE, 0x00, 0x07, 0x00000578)

    Jump('loc_3B9')

    def _loc_389(): pass

    label('loc_389')

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_3B9')

    def _loc_395(): pass

    label('loc_395')

    OP_99(0x00FE, 0x00, 0x07, 0x00000546)

    Jump('loc_3B9')

    def _loc_3A1(): pass

    label('loc_3A1')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_3B9')

    def _loc_3AD(): pass

    label('loc_3AD')

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_3B9')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_3B9')

    def _loc_3CE(): pass

    label('loc_3CE')

    Return()

# id: 0x0003 offset: 0x3CF
@scena.Code('func_03_3CF')
def func_03_3CF():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x3D4
@scena.Code('func_04_3D4')
def func_04_3D4():
    TalkBegin(0x0008)
    OP_A2(0x1007)

    If(
        (
            (Expr.Eval, "OP_40(0x02D6, 0x00)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0208, 1, 0x1041)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_52B',
    )

    ChrTalk(
        0x0008,
        (
            '#2760191069V啊，艾丝蒂尔……\n',
            '得到『天眼』了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2760191070V那可是所谓的\n',
            '高级结晶回路呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2760191071V要镶嵌它的话\n',
            '就必须先强化结晶孔才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2760191072V虽然需要耗费相对数量的耀晶片，\n',
            '不过也能提高最大ＥＰ，所以建议一试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2760191417V工房的菜单里\n',
            '选[改造·换钱]-[结晶孔]\n',
            '就能强化结晶孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)
    OP_A2(0x1041)
    TalkEnd(0x0008)

    Return()

    def _loc_52B(): pass

    label('loc_52B')

    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '买东西\n'),
            TXT(0x03, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_591',
    )

    OP_0D()
    OP_A9(0xFA)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A7',
    )

    OP_0D()
    OP_A9(0xFB)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_5A7(): pass

    label('loc_5A7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B8',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_5B8(): pass

    label('loc_5B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_652',
    )

    ChrTalk(
        0x0008,
        (
            '#2760191418V若不是强化过的结晶孔，\n',
            '就无法装配高级结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2760191419V但是，在战斗中应该会很有帮助。\n',
            '希望你们都能够事先强化结晶孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B1')

    def _loc_652(): pass

    label('loc_652')

    ChrTalk(
        0x0008,
        (
            '#2760191420V你们两人都要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2760191421V需要调整导力器的时候，\n',
            '请随时来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B1(): pass

    label('loc_6B1')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x6B5
@scena.Code('func_05_6B5')
def func_05_6B5():
    EventBegin(0x00)
    OP_6D(20200, 0, 18730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 18800, -800, 500, 0)
    SetChrPos(0x010A, 19720, -800, 500, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x010A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_0732')
    def lambda_0732():
        OP_6D(18420, -300, 3580, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0732)

    Sleep(2000)

    @scena.Lambda('lambda_074F')
    def lambda_074F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_074F)

    @scena.Lambda('lambda_0761')
    def lambda_0761():
        OP_8E(0x0101, 18800, -550, 2140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0761)

    Sleep(200)

    @scena.Lambda('lambda_0781')
    def lambda_0781():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x010A, 0x0002, lambda_0781)

    OP_8E(0x010A, 19720, -550, 1710, 2000, 0x00)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010191325V#1026F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191326V那枪，是克鲁茨前辈的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191327V#813F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x010A, 270, 500)
    Sleep(500)

    ChrTalk(
        0x010A,
        (
            '#0120191328V#810F总之……\n',
            '先调查宿舍里看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191329V说不定能找到\n',
            '什么线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 500)

    ChrTalk(
        0x0101,
        (
            '#0010191330V#1002F#6P嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x101C)
    OP_28(0x0080, 0x01, 0x0002)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0006 offset: 0x8DC
@scena.Code('func_06_8DC')
def func_06_8DC():
    EventBegin(0x00)
    Call(0, 0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_8EE',
    )

    EventEnd(0x00)

    Jump('loc_8F0')

    def _loc_8EE(): pass

    label('loc_8EE')

    EventEnd(0x01)

    def _loc_8F0(): pass

    label('loc_8F0')

    SetMapFlags(0x02000000)

    Return()

# id: 0x0007 offset: 0x8F6
@scena.Code('func_07_8F6')
def func_07_8F6():
    EventBegin(0x00)
    Call(0, 0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_908',
    )

    EventEnd(0x00)

    Jump('loc_90A')

    def _loc_908(): pass

    label('loc_908')

    EventEnd(0x01)

    def _loc_90A(): pass

    label('loc_90A')

    SetMapFlags(0x02000000)

    Return()

# id: 0x0008 offset: 0x910
@scena.Code('func_08_910')
def func_08_910():
    EventBegin(0x00)
    Call(0, 0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_922',
    )

    EventEnd(0x00)

    Jump('loc_924')

    def _loc_922(): pass

    label('loc_922')

    EventEnd(0x01)

    def _loc_924(): pass

    label('loc_924')

    SetMapFlags(0x02000000)

    Return()

# id: 0x0009 offset: 0x92A
@scena.Code('func_09_92A')
def func_09_92A():
    EventBegin(0x00)
    Call(0, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_93C',
    )

    EventEnd(0x00)

    Jump('loc_93E')

    def _loc_93C(): pass

    label('loc_93C')

    EventEnd(0x01)

    def _loc_93E(): pass

    label('loc_93E')

    SetMapFlags(0x02000000)

    Return()

# id: 0x000A offset: 0x944
@scena.Code('func_0A_944')
def func_0A_944():
    EventBegin(0x00)
    Call(0, 0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_956',
    )

    EventEnd(0x00)

    Jump('loc_958')

    def _loc_956(): pass

    label('loc_956')

    EventEnd(0x01)

    def _loc_958(): pass

    label('loc_958')

    SetMapFlags(0x02000000)

    Return()

# id: 0x000B offset: 0x95E
@scena.Code('func_0B_95E')
def func_0B_95E():
    EventBegin(0x00)
    Call(0, 0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_970',
    )

    EventEnd(0x00)

    Jump('loc_972')

    def _loc_970(): pass

    label('loc_970')

    EventEnd(0x01)

    def _loc_972(): pass

    label('loc_972')

    SetMapFlags(0x02000000)

    Return()

# id: 0x000C offset: 0x978
@scena.Code('func_0C_978')
def func_0C_978():
    SetChrFlags(0x000A, 0x0080)
    OP_64(0x09, 0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 １卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 １卷'], 1)
    OP_A2(0x10B5)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x9CF
@scena.Code('func_0D_9CF')
def func_0D_9CF():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '折断的枪滚落在地。\n',
            '看来是克鲁茨的武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Return()

# id: 0x000E offset: 0xA26
@scena.Code('func_0E_A26')
def func_0E_A26():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '窗户玻璃碎片散乱一地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 5, 0x101D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B09',
    )

    OP_A2(0x101D)
    OP_28(0x0080, 0x01, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010191331V#1015F这是昨天晚上\n',
            '猎兵闯入时留下的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191332V#812F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191333V那身体的动作……\n',
            '恐怕是经过了专门的训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B09(): pass

    label('loc_B09')

    Call(0, 0x0013)

    Return()

# id: 0x000F offset: 0xB0E
@scena.Code('func_0F_B0E')
def func_0F_B0E():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '通讯器被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 6, 0x101E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BE8',
    )

    OP_A2(0x101E)
    OP_28(0x0080, 0x01, 0x0008)

    ChrTalk(
        0x010A,
        (
            '#0120191334V#1316F不愧是职业佣兵。\n',
            '连这个都不放过吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191335V#1002F原来如此。\n',
            '不让我们求援吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191336V这可是重创……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE8(): pass

    label('loc_BE8')

    Call(0, 0x0013)

    Return()

# id: 0x0010 offset: 0xBED
@scena.Code('func_10_BED')
def func_10_BED():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '地上都是血污。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 7, 0x101F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CD1',
    )

    OP_A2(0x101F)
    OP_28(0x0080, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010191337V#1026F这个……\n',
            '难道是克鲁茨前辈的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191338V#813F嗯……\n',
            '很可能是前辈的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191339V从地面的血量判断，\n',
            '他并未受致命伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD1(): pass

    label('loc_CD1')

    Call(0, 0x0013)

    Return()

# id: 0x0011 offset: 0xCD6
@scena.Code('func_11_CD6')
def func_11_CD6():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放食材的罐子\n',
            '空了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 0, 0x1020)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB1',
    )

    OP_A2(0x1020)
    OP_28(0x0080, 0x01, 0x0020)

    ChrTalk(
        0x0101,
        (
            '#0010191340V#1004F这个……\n',
            '是敌人拿走的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191341V#812F嗯、嗯～\n',
            '很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191342V管理员也不在，\n',
            '到底怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DB1(): pass

    label('loc_DB1')

    Call(0, 0x0013)

    Return()

# id: 0x0012 offset: 0xDB6
@scena.Code('func_12_DB6')
def func_12_DB6():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像有什么东西被撕破了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 1, 0x1021)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E9C',
    )

    OP_A2(0x1021)
    OP_28(0x0080, 0x01, 0x0040)

    ChrTalk(
        0x0101,
        (
            '#0010191343V#1002F我记得这里\n',
            '好像贴着地图吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191344V#812F嗯，和我们\n',
            '持有的是一样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191345V#818F把那个拿走也就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E9C(): pass

    label('loc_E9C')

    Call(0, 0x0013)

    Return()

# id: 0x0013 offset: 0xEA1
@scena.Code('func_13_EA1')
def func_13_EA1():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 5, 0x101D)),
            Expr.Return,
        ),
        'loc_EBC',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_EBC(): pass

    label('loc_EBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 6, 0x101E)),
            Expr.Return,
        ),
        'loc_ECD',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_ECD(): pass

    label('loc_ECD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0203, 7, 0x101F)),
            Expr.Return,
        ),
        'loc_EDE',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_EDE(): pass

    label('loc_EDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 0, 0x1020)),
            Expr.Return,
        ),
        'loc_EEF',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_EEF(): pass

    label('loc_EEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 1, 0x1021)),
            Expr.Return,
        ),
        'loc_F00',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_F00(): pass

    label('loc_F00')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F0E',
    )

    Return()

    def _loc_F0E(): pass

    label('loc_F0E')

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0101, 21280, 0, 9960, 170)
    SetChrPos(0x010A, 22640, 0, 9100, 262)
    OP_6D(23000, 0, 10260, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3230, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191346V#1P#1015F大致已经把整个宿舍\n',
            '调查了一遍……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191347V二楼完全没有异常。\n',
            '被弄乱的似乎只有一楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191348V#2P#1316F嗯……\n',
            '应该有什么理由吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191349V#816F不过，敌人要做什么\n',
            '大体上明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191350V#1P#1004F咦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191351V#2P#812F敌人的行动虽然疑点众多\n',
            '却也有连贯的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191352V这个宿舍，还有森林的帐篷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191353V把两个地方发现的\n',
            '线索联系起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191354V#1P#1006F啊……难不成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '敌人采取的行动是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【从峡谷撤退了】\n'),
            TXT(0x01, '【封锁了峡谷的入口】\n'),
            TXT(0x02, '【向新的据点转移了】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_121C'),
        (0x00000001, 'loc_1341'),
        (0x00000002, 'loc_1432'),
        (-1, 'loc_14E9'),
    )

    def _loc_121C(): pass

    label('loc_121C')

    ChrTalk(
        0x010A,
        (
            '#0120191355V#2P#813F不，我想不会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191356V如果撤退了，应该没有\n',
            '把前辈们带走的必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191357V#1P#1007F啊，那倒也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191358V#2P#812F大概在森林里的帐篷\n',
            '是为了袭击这个宿舍\n',
            '而建造的临时据点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191359V这样的话……\n',
            '那里人烟稀少，\n',
            '想必是转移到其他据点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_1341(): pass

    label('loc_1341')

    OP_2B(0x007E, 0x0001)

    ChrTalk(
        0x010A,
        (
            '#0120191360V#2P#817F嗯……\n',
            '这个可能性很高哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191361V#810F不过，还有比这\n',
            '更确定的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191362V多半森林里的帐篷\n',
            '是为了袭击这个宿舍\n',
            '而建造的临时据点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191359V这样的话……\n',
            '那里人烟稀少，\n',
            '想必是转移到其他据点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E9')

    def _loc_1432(): pass

    label('loc_1432')

    OP_2B(0x007E, 0x0003)

    ChrTalk(
        0x010A,
        (
            '#0120191364V#2P#810F嗯，我也这么想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191362V多半森林里的帐篷\n',
            '是为了袭击这个宿舍\n',
            '而建造的临时据点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191359V这样的话……\n',
            '那里人烟稀少，\n',
            '想必是转移到其他据点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14E9(): pass

    label('loc_14E9')

    ChrTalk(
        0x0101,
        (
            '#0010191367V#1P#1004F啊，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191368V#1015F不过，不打算\n',
            '用这个宿舍当据点了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191369V#2P#812F从昨天的袭击也能看出来，\n',
            '这里的防守不太稳固。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191370V万一，协会的支援来了，\n',
            '那能和人质一起隐藏起来的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191371V应该是把据点\n',
            '移往这样的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191372V#1P#1006F嗯嗯。\n',
            '这样考虑似乎很合理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191373V如果是这样，\n',
            '他们转移的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, 20220, -550, 0, 181)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#2760191374V#1P你、你们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_16DB')
    def lambda_16DB():
        OP_6D(22240, -300, 7440, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16DB)

    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x010A, 0x0008, 400)
    OP_4A(0x0008, 255)
    OP_9F(0x0008, 0x00, 0x00, 0x00, 0x00, 0x00000000)
    ClearChrFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_1715')
    def lambda_1715():
        OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1715)

    OP_8E(0x0008, 20250, -550, 1960, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x010A,
        (
            '#0120191375V#814F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191376V#1004F罗伯特先生！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191377V#1018F没、没事吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17AD')
    def lambda_17AD():
        OP_8E(0x00FE, 22490, -300, 6940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_17AD)

    Sleep(100)

    @scena.Lambda('lambda_17CD')
    def lambda_17CD():
        OP_8E(0x00FE, 21160, -300, 7040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_17CD)

    Sleep(200)

    @scena.Lambda('lambda_17ED')
    def lambda_17ED():
        OP_8E(0x00FE, 21300, -300, 5310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_17ED)

    WaitForThreadExit(0x010A, 0x0000)
    OP_8C(0x010A, 224, 500)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0008, 0x0000)

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191378V昨夜，克鲁茨前辈\n',
            '看准间隙让我逃走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191379V之前一直想办法躲着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191380V#1P#1008F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191381V#5P#1314F太好了……\n',
            '他平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191382V抱歉……\n',
            '我竟然一个人逃跑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191383V真是的……\n',
            '身为男人实在是太丢脸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191384V#1P#1016F别、别消沉啦～\n',
            '毕竟对方是职业的佣兵嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191385V#5P#1310F嗯嗯，就是说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191386V没有成为人质\n',
            '就已经很幸运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191387V是吗……\n',
            '听你们这么说，我心里好受多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191388V那么最后，克鲁茨前辈\n',
            '和管理员去哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191389V#1P#1003F这、这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说出了敌方集团将两人\n',
            '转移到其它据点的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191390V原来如此……\n',
            '容易守卫的据点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191391V这么说来……\n',
            '不就是『格林姆瑟尔小要塞』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191392V#1P#1004F要、要塞！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191393V#5P#814F这、这附近有那种东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191394V虽说是要塞，\n',
            '但并不是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191395V是最近才刚刚建造而成的，\n',
            '模仿军事设施的训练设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191396V主要用做反恐训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191397V#1P#1015F还、还有这种地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010A, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191398V#6P#1002F……亚妮拉丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010A, 0x0101, 500)

    ChrTalk(
        0x010A,
        (
            '#0120191399V#5P#816F嗯……明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191400V喂、喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191401V你们两个该不是\n',
            '打算挑战那个集团吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191402V还是联络协会\n',
            '求援比较好吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 500)
    ChrTurnDirection(0x010A, 0x0008, 500)

    ChrTalk(
        0x0101,
        (
            '#0010191403V#1P#1002F啊、通信器坏掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191404V…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191405V#5P#812F嗯，罗伯特先生\n',
            '通讯器的修理就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191406V一修好就通知协会\n',
            '向他们求援行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191407V……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191408V如果需要整备导力器\n',
            '就到工房来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '维修师罗伯特',
        (
            '#2760191409V那么祝你们好运！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F59')
    def lambda_1F59():
        OP_6D(24810, 0, 6590, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1F59)

    @scena.Lambda('lambda_1F71')
    def lambda_1F71():
        OP_8E(0x00FE, 23540, 0, 5860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1F71)

    OP_8C(0x0101, 89, 500)
    OP_8C(0x010A, 89, 500)
    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_1F9F')
    def lambda_1F9F():
        OP_8E(0x00FE, 24730, 0, 6840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1F9F)

    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_1FBF')
    def lambda_1FBF():
        OP_8E(0x00FE, 26830, 0, 6890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1FBF)

    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_1FDF')
    def lambda_1FDF():
        OP_8E(0x00FE, 26690, 0, 5140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1FDF)

    WaitForThreadExit(0x0008, 0x0000)
    OP_8C(0x0008, 258, 500)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_2012')
    def lambda_2012():
        OP_6D(22920, -300, 7620, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2012)

    OP_4B(0x0008, 255)
    OP_65(0x00, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x010A, 262, 500)

    ChrTalk(
        0x010A,
        (
            '#0120191410V#2P#816F好了……\n',
            '走吧，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191411V去那个『格林姆瑟尔小要塞』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191412V#6P#1018F喔，明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1022)
    OP_28(0x0080, 0x01, 0x0080)
    OP_28(0x0080, 0x01, 0x0100)
    OP_28(0x0080, 0x01, 0x0200)
    OP_65(0x07, 0x0001)
    OP_65(0x08, 0x0001)

    Return()

# id: 0x0014 offset: 0x20DA
@scena.Code('func_14_20DA')
def func_14_20DA():
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_215F',
    )

    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    OP_8C(0x0000, 270, 0)
    OP_30(0x00)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_0D()
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_215F(): pass

    label('loc_215F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2179',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_2179(): pass

    label('loc_2179')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
