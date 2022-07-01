import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5600_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5600   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '小丑肯帕雷拉'),
    TXT(0x02, '银发的青年'),
    TXT(0x03, '怀斯曼教授'),
    TXT(0x04, '歼灭天使玲'),
    TXT(0x05, '高速飞艇'),
    TXT(0x06, '帕蒂尔·玛蒂尔'),
    TXT(0x07, '目标用照相机'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5600.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C79
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
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT26/CH20295._CH', 'ED6_DT26/CH20295P._CP'),
        ('ED6_DT26/CH20305._CH', 'ED6_DT26/CH20305P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 9520,
            triggerZ            = 9000,
            triggerY            = 6150,
            triggerRange        = 1000,
            actorX              = 9960,
            actorZ              = 9000,
            actorY              = 6600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x22E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_244',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    Jump('loc_251')

    def _loc_244(): pass

    label('loc_244')

    Event(0, 0x0004)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_251(): pass

    label('loc_251')

    Return()

# id: 0x0001 offset: 0x252
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDDD20, 0xFFFE3AE0, 0x00230073)
    OP_22(0x01C5, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A5, 0, 0x1D28)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27B',
    )

    OP_6F(0x0001, 0)

    Jump('loc_282')

    def _loc_27B(): pass

    label('loc_27B')

    OP_6F(0x0001, 60)

    def _loc_282(): pass

    label('loc_282')

    Return()

# id: 0x0002 offset: 0x283
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_298',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_298(): pass

    label('loc_298')

    Return()

# id: 0x0003 offset: 0x299
@scena.Code('func_03_299')
def func_03_299():
    UnlockAchievement(0x02, 0x9E, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A5, 0, 0x1D28)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_376',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['催眠曲奇'], 1)"),
            Expr.Return,
        ),
        'loc_30D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D28)

    Jump('loc_373')

    def _loc_30D(): pass

    label('loc_30D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_373(): pass

    label('loc_373')

    Jump('loc_3A7')

    def _loc_376(): pass

    label('loc_376')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_3A7(): pass

    label('loc_3A7')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FF',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0043)"),
            Expr.Return,
        ),
        'loc_3C6',
    )

    Jump('loc_3FF')

    def _loc_3C6(): pass

    label('loc_3C6')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['催眠曲奇']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FF(): pass

    label('loc_3FF')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x408
@scena.Code('func_04_408')
def func_04_408():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x010A, 0x0080)
    OP_6D(2380, 30000, -14320, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(340000, 0)
    OP_6E(730, 0)
    OP_11(0xA0, 0xB4, 0xFF, 0x00003A98, 0x00030D40, 0x00000000)
    SetChrPos(0x0101, -26000, 18450, 11200, 180)
    SetChrPos(0x0008, -26000, 18450, 11200, 180)
    OP_A1(0x000C, 0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 700)
    OP_70(0x0000, 0x0000030C)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0040)
    SetChrPos(0x000C, 21380, 20000, -38500, 0)
    OP_97(0x000C, 0x00004B6E, 0x000004A6, 0x000003E8, 0x00002710, 0x0001)

    @scena.Lambda('lambda_04DC')
    def lambda_04DC():
        OP_6C(330000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_04DC)

    @scena.Lambda('lambda_04EC')
    def lambda_04EC():
        OP_67(0, 12010, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_04EC)

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#50A同一时刻。\n',
            '利贝尔王国，某处──',
            TxtCtl.Enter,
        ),
    )

    Sleep(100)

    FadeIn(1000, 0)
    Sleep(3000)

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    OP_22(0x0079, 0x00, 0x64)
    Fade(1000)
    TerminateThread(0x0008, 0xFF)
    OP_6D(-31780, 30000, -16820, 0)
    OP_67(0, 8060, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(59000, 0)
    OP_6E(697, 0)
    OP_0D()

    @scena.Lambda('lambda_05B3')
    def lambda_05B3():
        OP_6D(-31780, 25000, 5000, 5000)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_05B3)

    OP_97(0x000C, 0x00004B6E, 0x000004A6, 0x000057E4, 0x00003E80, 0x0001)
    OP_97(0x000C, 0x00004B6E, 0x000004A6, 0x000057E4, 0x00003A98, 0x0001)
    OP_97(0x000C, 0x00004B6E, 0x000004A6, 0x000057E4, 0x000036B0, 0x0001)
    OP_97(0x000C, 0x00004B6E, 0x000004A6, 0x00004E20, 0x000032C8, 0x0001)
    OP_8C(0x000C, 0, 400)
    SetChrFlags(0x000C, 0x0001)
    ClearChrFlags(0x000C, 0x0080)

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x34,
        (
            (Expr.PushLong, 0x1ADB0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 780)
    OP_70(0x0000, 0x00000320)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 0x00000384)

    @scena.Lambda('lambda_0686')
    def lambda_0686():
        OP_8F(0x00FE, -25800, 15150, 11920, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0686)

    Sleep(1500)

    OP_22(0x00CC, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x000C, 0x0001)
    OP_72(0x0000, 0x0020)
    OP_D8(0x00, 0x01F4)
    OP_82(0x01, 0x02)
    OP_6F(0x0000, 1000)
    OP_70(0x0000, 0x0000041A)
    OP_73(0x0000)
    Sleep(200)

    OP_6F(0x0000, 1050)
    OP_70(0x0000, 0x00000456)
    OP_73(0x0000)
    OP_23(0x0079)
    OP_23(0x00CC)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00000064)
    Fade(1000)
    OP_6D(-13700, 30000, 8590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(296000, 0)
    OP_6E(409, 0)
    OP_0D()
    OP_22(0x0076, 0x00, 0x64)
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 1110)
    OP_70(0x0000, 0x00000474)
    OP_73(0x0000)
    OP_B0(0x0000, 0x3C)
    OP_6F(0x0000, 1140)
    OP_70(0x0000, 0x000004B0)
    Sleep(200)

    OP_22(0x00FD, 0x00, 0x64)
    OP_73(0x0000)
    Sleep(500)

    SetChrBattleFlags(0x0008, 0x0020)
    ClearChrFlags(0x0008, 0x0080)
    OP_12(0x0000EA60, 0x00030D40, 0x00001770)

    @scena.Lambda('lambda_07CC')
    def lambda_07CC():
        OP_6D(-25090, 15200, -1540, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_07CC)

    @scena.Lambda('lambda_07E4')
    def lambda_07E4():
        OP_67(0, 11430, -18000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_07E4)

    @scena.Lambda('lambda_07FC')
    def lambda_07FC():
        OP_6B(2090, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_07FC)

    @scena.Lambda('lambda_080C')
    def lambda_080C():
        OP_6C(0, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_080C)

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        OP_6E(230, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_081C)

    OP_8E(0x0008, -25370, 15000, -1480, 2000, 0x00)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    Sleep(500)

    NpcTalk(
        0x0008,
        '奇怪的少年',
        (
            '#0190191653V#5P#850F哟。\n',
            '很棒的地方嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191654V#5P教授的品味还真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, -16600, 15000, 4170, 237)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0009, 0x0080)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0140191655V#3P你真慢啊，肯帕雷拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_093F')
    def lambda_093F():
        OP_6D(-21040, 15200, 1680, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_093F)

    @scena.Lambda('lambda_0957')
    def lambda_0957():
        OP_6B(2300, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0957)

    ChrTurnDirection(0x0008, 0x0009, 500)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_0978')
    def lambda_0978():
        OP_92(0x0009, 0x0008, 0x000007D0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0978)

    Sleep(500)

    @scena.Lambda('lambda_0992')
    def lambda_0992():
        OP_69(0x0008, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0992)

    @scena.Lambda('lambda_09A0')
    def lambda_09A0():
        OP_6C(270000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09A0)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0000)
    ChrTurnDirection(0x0008, 0x0009, 500)

    ChrTalk(
        0x0008,
        (
            '#0190191656V#851F呀，『剑帝』。\n',
            '好久不见啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191657V你不在的这半年间，\n',
            '我真是寂寞难耐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191658V#124F哼，口是心非。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191659V#123F对帝国游击士协会的袭击，\n',
            '听说是由你负责的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191660V作为卡西乌斯·布莱特的对手，\n',
            '想必你相当地开心吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191661V#850F什么啊，原来你知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191662V#851F呀～那位大叔\n',
            '真是个不得了的人物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191663V明明应该不知道我的存在，\n',
            '却能采取一连串正确的对策。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191664V托他的福，我手中的猎兵团\n',
            '被消灭了一支。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191665V#124F『杰斯塔猎兵团』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191666V#120F虽然也训练了一下，\n',
            '但毕竟还是些平庸之辈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191667V要作为『剑圣』的对手，\n',
            '担子稍微重了点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191668V#853F不过，能拖住他的行动\n',
            '直到你的工作完成，算是很不错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191669V#850F哎呀，难道你\n',
            '很期待和他的对决吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191670V#123F呵呵……一点点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191671V#124F不过，山中的猛虎\n',
            '也被名为军务的锁链束缚住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191672V从正面进攻的话，\n',
            '已经不可能阻止我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191673V#850F呵呵，教授的计划\n',
            '看来进行得很顺利呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191674V那么，其它的成员\n',
            '都来到利贝尔了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191675V#120F啊啊，昨天才刚刚集合。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191676V#124F布卢布兰那家伙，\n',
            '好像老早就过来准备了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191677V『怪盗绅士』、『瘦狼』、\n',
            '『幻惑之铃』、『歼灭天使』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191678V#123F跑来的偏偏\n',
            '都是些古怪的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191679V#851F嘻嘻，你不也是\n',
            '相当古怪嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191680V#854F话说回来，『他』……\n',
            '听说现在行踪不明了，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191681V#120F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191682V#854F嘻嘻，真是期待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191683V在我们『执行者』当中，\n',
            '他的隐秘行动也算首屈一指的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191684V面对『剑帝』和『白面』，\n',
            '他能努力到什么程度呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191685V#121F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191686V#124F毕竟是好几年前\n',
            '就从结社洗手不干的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191687V应该不会成为多大的威胁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000A, -17000, 15200, 8000, 226)
    ClearChrFlags(0x000A, 0x0080)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0150191688V#1P不不。\n',
            '我认为没有这回事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x000A, 500)
    Sleep(500)

    Fade(1000)
    OP_6D(-20220, 15200, 2810, 0)
    OP_67(0, 11430, -18000, 0)
    OP_6B(2390, 0)
    OP_6C(0, 0)
    OP_6E(230, 0)
    SetChrPos(0x000A, -18440, 15000, 4740, 229)
    SetChrPos(0x0009, -24430, 15000, 240, 41)
    SetChrPos(0x0008, -24930, 15000, -1890, 24)

    @scena.Lambda('lambda_1183')
    def lambda_1183():
        ChrTurnDirection(0x0009, 0x000A, 500)
        Yield()

        Jump('lambda_1183')

    DispatchAsync2(0x0009, 0x0001, lambda_1183)

    ChrTurnDirection(0x0008, 0x000A, 500)

    @scena.Lambda('lambda_119B')
    def lambda_119B():
        OP_6D(-23900, 15000, -700, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_119B)

    OP_8E(0x000A, -23300, 15000, -440, 2000, 0x00)
    OP_0D()
    WaitForThreadExit(0x000A, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0150191689V#2P#1150F呀，肯帕雷拉。\n',
            '还劳烦你特地过来一趟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150191690V你成功地拖延了卡西乌斯·布莱特\n',
            '的行动，真是帮了我一个大忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191691V#851F#6P嘻嘻，这是份很愉快的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191692V#850F不过教授的计划书\n',
            '我拜读过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191693V这实在是相当\n',
            '令人愉快的想法嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0150191694V#2P#1151F哈哈哈，能让你这个小丑\n',
            '这么说，真是我的荣幸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150191695V不过，实际的计划\n',
            '将会更加令人期待哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150191696V毕竟前来参与这次行动的诸位，\n',
            '每个人都拥有各自的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150191697V我、还有这位也是一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140191698V#124F#5P……我不否定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140191699V#121F我可没有受你\n',
            '暗示影响的道理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0150191700V#2P#1154F哎呀哎呀，真冷淡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191701V#851F#6P呵呵，原来如此。\n',
            '看来似乎有不少的隐情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191702V#854F算了，教授的恶趣味\n',
            '已经可以称得上是艺术了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191703V就让我尽情地享受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0150191704V#2P#1151F呵呵……\n',
            '说什么恶趣味，多难听啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150191705V算了，你就尽情地\n',
            '欣赏本次的计划吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150191706V以我们『盟主』的代理人身份。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0190191707V#851F#6P嘻嘻，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    TerminateThread(0x0009, 0xFF)
    OP_8C(0x0009, 187, 0)
    OP_8C(0x000A, 235, 0)
    OP_6D(-25190, 15200, -2240, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(215000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x03, 0x000005DC)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0190191708V#853F#5P执行者Ｎｏ.０──\n',
            '『小丑』肯帕雷拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190191709V#854F现在开始观察使徒\n',
            '怀斯曼的『福音计划』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    Sleep(300)

    OP_24(0x01C5, 0x5A)
    Sleep(300)

    OP_24(0x01C5, 0x50)
    Sleep(300)

    OP_24(0x01C5, 0x46)
    Sleep(300)

    OP_24(0x01C5, 0x3C)
    Sleep(300)

    OP_24(0x01C5, 0x32)
    Sleep(300)

    OP_24(0x01C5, 0x28)
    Sleep(300)

    OP_24(0x01C5, 0x1E)
    Sleep(300)

    OP_24(0x01C5, 0x14)
    Sleep(300)

    OP_24(0x01C5, 0x0A)
    Sleep(300)

    OP_24(0x01C5, 0x00)
    OP_21()
    Sleep(1000)

    NewScene('ED6_DT21/T5200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x1720
@scena.Code('func_05_1720')
def func_05_1720():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1733',
    )

    Call(0, 0x0006)

    def _loc_1733(): pass

    label('loc_1733')

    OP_71(0x0000, 0x0004)
    OP_6D(-13460, 15200, -850, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(6010, 0)
    OP_6C(0, 0)
    OP_6E(598, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, -26000, 18450, 11200, 180)
    OP_A1(0x000D, 0x0002)
    OP_71(0x0002, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x0F)
    OP_6F(0x0002, 501)
    OP_70(0x0002, 0x00000208)
    SetChrFlags(0x000B, 0x0020)
    SetChrFlags(0x000B, 0x0002)
    OP_CF(0x000B, 0x02, 'Frame85__ren')
    OP_8C(0x000B, 180, 0)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0040)
    SetChrPos(0x000D, 21380, 20000, -38500, 0)
    OP_97(0x000D, 0x00004B6E, 0x000004A6, 0x000003E8, 0x00002710, 0x0001)

    @scena.Lambda('lambda_1813')
    def lambda_1813():
        OP_6D(-23730, 15200, 7580, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1813)

    @scena.Lambda('lambda_182B')
    def lambda_182B():
        OP_67(0, 7830, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_182B)

    @scena.Lambda('lambda_1843')
    def lambda_1843():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1843)

    @scena.Lambda('lambda_1853')
    def lambda_1853():
        OP_6B(4200, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1853)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_22(0x0079, 0x00, 0x64)
    OP_97(0x000D, 0x00004B6E, 0x000004A6, 0x000057E4, 0x00003E80, 0x0001)
    OP_97(0x000D, 0x00004B6E, 0x000004A6, 0x000057E4, 0x00003A98, 0x0001)
    OP_97(0x000D, 0x00004B6E, 0x000004A6, 0x000057E4, 0x000036B0, 0x0001)
    OP_97(0x000D, 0x00004B6E, 0x000004A6, 0x00004E20, 0x000032C8, 0x0001)
    OP_8C(0x000D, 0, 400)
    OP_72(0x0002, 0x0020)
    OP_B0(0x0002, 0x0A)
    OP_6F(0x0002, 500)
    OP_70(0x0002, 0x000001E1)

    @scena.Lambda('lambda_18E9')
    def lambda_18E9():
        OP_8F(0x00FE, -25800, 20000, 11920, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_18E9)

    Sleep(1500)

    WaitForThreadExit(0x000D, 0x0001)
    OP_8C(0x000D, 90, 50)
    Fade(1000)
    OP_6D(-27510, 15200, 10990, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000B, 0x0001)
    SetChrPos(0x000D, -24960, 18450, 7270, 90)

    @scena.Lambda('lambda_1972')
    def lambda_1972():
        OP_8F(0x00FE, -24800, 15300, 7220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1972)

    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 421)
    OP_70(0x0002, 0x000001CC)
    OP_0D()
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x0000012C, 0x00000FA0, 0x000001F4)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 421)
    OP_23(0x0079)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#260F哈哈哈，把那些野猪一样的\n',
            '飞艇全部甩开了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F谢谢你，『帕蒂尔·玛蒂尔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, -12840, 14800, 9830, 270)
    ClearChrFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0140271104V#1P终于回来了，玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_1AB6')
    def lambda_1AB6():
        OP_6D(-20330, 15200, 9930, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1AB6)

    Sleep(500)

    @scena.Lambda('lambda_1AD3')
    def lambda_1AD3():
        OP_8E(0x00FE, -15790, 15200, 9170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1AD3)

    ClearChrFlags(0x000B, 0x0020)
    ClearChrFlags(0x000B, 0x0002)
    OP_8C(0x000B, 180, 400)
    WaitForThreadExit(0x0009, 0x0000)
    OP_8C(0x0009, 270, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000B,
        (
            '#260F莱维！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000B, 0x0020)
    ClearChrFlags(0x000B, 0x0002)
    OP_CF(0x000B, 0x02, 'Frame86__ren')
    OP_8C(0x000B, 90, 0)
    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x000B, 0xFFFFAFC4, 0x00003B60, 0x0000240E, 0x00000258, 0x000005DC)
    SetChrFlags(0x000B, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_1B69')
    def lambda_1B69():
        OP_8E(0x00FE, -17230, 15200, 9040, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B69)

    @scena.Lambda('lambda_1B84')
    def lambda_1B84():
        OP_6D(-16620, 15200, 9110, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1B84)

    @scena.Lambda('lambda_1B9C')
    def lambda_1B9C():
        OP_67(0, 5290, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B9C)

    @scena.Lambda('lambda_1BB4')
    def lambda_1BB4():
        OP_6B(3420, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BB4)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x000B,
        (
            '#260F嘿嘿，我回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271107V玲可是按照你的吩咐，\n',
            '成功做完了实验哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F呵呵，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271109V不过你把事情搞得\n',
            '还真是大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F因为这次说是\n',
            '不能杀人嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这么无聊\n',
            '至少要热闹热闹嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271112V托你的福\n',
            '开了个很开心的茶会哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F呵呵……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '实验的结果怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F这个嘛。\n',
            '还算不错吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然被教会的哥哥\n',
            '给搅了一下局……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271117V但运作很稳定，\n',
            '我想足够用于实战了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F嗯，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F不过『福音』\n',
            '现在还不能量产吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271120V能否作为兵器使用，\n',
            '现在还无法确定呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140271121V#120F没有量产的必要啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271122V此次的实验也是\n',
            '单纯以测试新型\n',
            '福音的潜在能力为目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271123V并不是以制作兵器\n',
            '为目的的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F咦，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '算了。\n',
            '我也没什么兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，话说回来……\n',
            '约修亚还没找到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们为了扰乱军队而放出的\n',
            '人形兵器被破坏了好几架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271129V恐怕就是他干的好事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F嗯～真有一手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271131V虽然玲也很擅长捉迷藏，\n',
            '但还是敌不过约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊～啊，不好玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271133V为什么不干脆\n',
            '返回结社呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F谁知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F这么说来教授倒是\n',
            '说过由于艾丝蒂尔的原因\n',
            '约修亚才不会回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271136V艾丝蒂尔好像也在\n',
            '寻找约修亚呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271137V到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140271138V#120F玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271139V教授说的话\n',
            '还是不要盲目相信的好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F所谓真相\n',
            '每个人的看法都不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271142V譬如月亮的脸\n',
            '被大家比喻成各种各样的形态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F比如小兔子啦，或者螃蟹之类的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140271144V#120F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271145V教授所讲出来的“真实”\n',
            '和玲自己感悟到的“真实”是不同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271146V你一定要自己去看，自己去感受，\n',
            '只有这样才能体会到属于玲自己的“真实”。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F嗯～听起来好深奥哦，\n',
            '玲不是很明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过玲好像确实\n',
            '挺喜欢艾丝蒂尔她们…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271149V就算下次再见面，\n',
            '大概也不会马上就杀死她们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F那就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你很了不起哦，玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0009, -16600, 15200, 9060, 2000, 0x00)
    Fade(250)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 14)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    OP_99(0x0009, 0x00, 0x02, 0x000003E8)
    OP_99(0x0009, 0x03, 0x06, 0x000003E8)
    OP_99(0x0009, 0x03, 0x06, 0x000003E8)
    Fade(250)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0002)
    SetChrChipByIndex(0x0009, 11)
    SetChrSubChip(0x0009, 0)
    OP_0D()
    OP_8F(0x0009, -15790, 15200, 9170, 2000, 0x00)

    ChrTalk(
        0x000B,
        (
            '#260F嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000A, -7420, 15000, 13980, 270)
    SetChrPos(0x0008, -7990, 15000, 14810, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0080)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0150271153V#1P呵呵，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_23D8')
    def lambda_23D8():
        OP_8E(0x00FE, -17250, 15200, 7900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_23D8)

    @scena.Lambda('lambda_23F3')
    def lambda_23F3():
        OP_8E(0x00FE, -15420, 15200, 8540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_23F3)

    Sleep(500)

    @scena.Lambda('lambda_2413')
    def lambda_2413():
        OP_8E(0x00FE, -15300, 15200, 9860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2413)

    @scena.Lambda('lambda_242E')
    def lambda_242E():
        OP_6D(-16030, 15200, 9710, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_242E)

    @scena.Lambda('lambda_2446')
    def lambda_2446():
        OP_6C(32000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2446)

    @scena.Lambda('lambda_2456')
    def lambda_2456():
        OP_6B(3290, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2456)

    WaitForThreadExit(0x0009, 0x0001)
    OP_8C(0x0009, 90, 400)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000B,
        (
            '#260F教授……\n',
            '还有肯帕雷拉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0221150001V你也来了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0191200001V#850F呼呼，前几天刚到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0191200002V你在王都似乎\n',
            '过得相当愉快啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F嘿嘿嘿，还好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要是事先知道你要来的话，\n',
            '绝对会招待你一起参加的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271159V当时的场面可是非常热闹的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2611',
    )

    ChrTalk(
        0x0008,
        (
            '#850F呵呵，那可真是遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271161V我也请游击士大姐姐她们\n',
            '看了场人偶剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271162V但比起你的茶会来，\n',
            '实在是不值一提啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_269A')

    def _loc_2611(): pass

    label('loc_2611')

    ChrTalk(
        0x0008,
        (
            '#850F呵呵，那可真是遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271164V我也请游击士大哥哥他们\n',
            '看了场人偶剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190271162V但比起你的茶会来，\n',
            '实在是不值一提啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_269A(): pass

    label('loc_269A')

    ChrTalk(
        0x000A,
        (
            '#0151850006V#1150F哈哈，下次有机会\n',
            '再请我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0151850007V不过玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271168V你好像和艾丝蒂尔\n',
            '相当投缘吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F嘿嘿，还好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '并不像教授说的那么讨厌，\n',
            '是个还挺不错的大姐姐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0151850008V#1150F哈哈，我也没\n',
            '说过她是个讨厌的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271172V实话说，倒真是一个性格善良，\n',
            '魅力十足的小姑娘呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0151850009V只是，约修亚之所以不愿意回来，\n',
            '原因确实是因为她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271174V对吧，莱维？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0141070019V#120F我不否认这是原因之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070020V但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0151850010V#1150F如何，玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271177V如果艾丝蒂尔成为我们的同伴，\n',
            '你会不会很高兴？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#260F让艾丝蒂尔成为同伴？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……嘻嘻。\n',
            '那当然好啊！很好玩的样子！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然实力还差得很远，\n',
            '但只要经过锻炼，应该也会很快变强吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220271182V而且，如果艾丝蒂尔加入的话，\n',
            '约修亚也会回来对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0151850011V#1150F呵呵，这是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#850F啊哈哈，不愧是教授。\n',
            '你还真是有兴致呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#120F教授，玩笑开过头了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '即使是你，\n',
            '也不能无视本人的意志，\n',
            '强行将她拉入结社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140271187V这可是『盟主』制定的`\n',
            '『噬身之蛇』规约。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0151850012V#1150F哼哼，这自然不用你说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271189V你以为身为『蛇之使徒』的我\n',
            '会做出那种事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271190V包括你和约修亚在内，\n',
            '我也没有强迫过任何人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0140271191V#120F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0151850013V#1150F要是那么做的话，\n',
            '难得的乐趣就都被破坏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150271193V必须让她完全自愿地\n',
            '加入我们才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x2BE4
@scena.Code('func_06_2BE4')
def func_06_2BE4():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_2C5E'),
        (0x00000001, 'loc_2C64'),
        (-1, 'loc_2C6A'),
    )

    def _loc_2C5E(): pass

    label('loc_2C5E')

    OP_A2(0x1200)

    Jump('loc_2C6A')

    def _loc_2C64(): pass

    label('loc_2C64')

    OP_A2(0x1201)

    Jump('loc_2C6A')

    def _loc_2C6A(): pass

    label('loc_2C6A')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
