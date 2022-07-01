import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '古代魔蜥'),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5201.x'
    header.mapIndex       = 1
    header.bgm            = 63
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA32
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
        ('ED6_DT29/CH12950._CH', 'ED6_DT29/CH12950P._CP'),
        ('ED6_DT29/CH12951._CH', 'ED6_DT29/CH12951P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12001._CH', 'ED6_DT29/CH12001P._CP'),
        ('ED6_DT29/CH12960._CH', 'ED6_DT29/CH12960P._CP'),
        ('ED6_DT29/CH12961._CH', 'ED6_DT29/CH12961P._CP'),
        ('ED6_DT29/CH12962._CH', 'ED6_DT29/CH12962P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 12860,
            z                   = 6000,
            y                   = -184960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x112
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -97710,
            z           = 0,
            y           = 64019,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34000,
            z           = 0,
            y           = -185250,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 126250,
            z           = 4000,
            y           = -186970,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 136370,
            z           = 4000,
            y           = -203580,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x043B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x182
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1220,
            y           = 0,
            z           = -181040,
            range       = 2840,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFD12E6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x1A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -50270,
            triggerZ            = 0,
            triggerY            = 52050,
            triggerRange        = 1000,
            actorX              = -49650,
            actorZ              = 0,
            actorY              = 52050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -50090,
            triggerZ            = 0,
            triggerY            = 16090,
            triggerRange        = 1000,
            actorX              = -49470,
            actorZ              = 0,
            actorY              = 16090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 7, 0x22FF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_208',
    )

    SetChrPos(0x0008, 12860, 6000, -184960, 270)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_208(): pass

    label('loc_208')

    Return()

# id: 0x0001 offset: 0x209
@scena.Code('Init')
def Init():
    Call(0, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 1, 0x2309)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F',
    )

    OP_6F(0x0008, 0)

    Jump('loc_226')

    def _loc_21F(): pass

    label('loc_21F')

    OP_6F(0x0008, 60)

    def _loc_226(): pass

    label('loc_226')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 2, 0x230A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_238',
    )

    OP_6F(0x0009, 0)

    Jump('loc_23F')

    def _loc_238(): pass

    label('loc_238')

    OP_6F(0x0009, 60)

    def _loc_23F(): pass

    label('loc_23F')

    Return()

# id: 0x0002 offset: 0x240
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_255',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_255(): pass

    label('loc_255')

    Return()

# id: 0x0003 offset: 0x256
@scena.Code('func_03_256')
def func_03_256():
    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_27F'),
        (0x00000003, 'loc_28C'),
        (0x00000004, 'loc_299'),
        (0x00000005, 'loc_2A6'),
        (0x00000006, 'loc_2B3'),
        (0x00000007, 'loc_2C0'),
        (0x00000008, 'loc_2CD'),
        (0x0000000A, 'loc_2DA'),
        (-1, 'loc_2E7'),
    )

    def _loc_27F(): pass

    label('loc_27F')

    OP_D2(0x000701D0, 0x000701DC, 0x09)

    Jump('loc_2E7')

    def _loc_28C(): pass

    label('loc_28C')

    OP_D2(0x000701E8, 0x000701F4, 0x09)

    Jump('loc_2E7')

    def _loc_299(): pass

    label('loc_299')

    OP_D2(0x0027036E, 0x0027037B, 0x09)

    Jump('loc_2E7')

    def _loc_2A6(): pass

    label('loc_2A6')

    OP_D2(0x00070218, 0x00070224, 0x09)

    Jump('loc_2E7')

    def _loc_2B3(): pass

    label('loc_2B3')

    OP_D2(0x00070230, 0x0007023C, 0x09)

    Jump('loc_2E7')

    def _loc_2C0(): pass

    label('loc_2C0')

    OP_D2(0x00070248, 0x00070254, 0x09)

    Jump('loc_2E7')

    def _loc_2CD(): pass

    label('loc_2CD')

    OP_D2(0x00270176, 0x00270183, 0x09)

    Jump('loc_2E7')

    def _loc_2DA(): pass

    label('loc_2DA')

    OP_D2(0x000702B4, 0x000702BB, 0x09)

    Jump('loc_2E7')

    def _loc_2E7(): pass

    label('loc_2E7')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_310'),
        (0x00000003, 'loc_31D'),
        (0x00000004, 'loc_32A'),
        (0x00000005, 'loc_337'),
        (0x00000006, 'loc_344'),
        (0x00000007, 'loc_351'),
        (0x00000008, 'loc_35E'),
        (0x0000000A, 'loc_36B'),
        (-1, 'loc_378'),
    )

    def _loc_310(): pass

    label('loc_310')

    OP_D2(0x000701D0, 0x000701DC, 0x0A)

    Jump('loc_378')

    def _loc_31D(): pass

    label('loc_31D')

    OP_D2(0x000701E8, 0x000701F4, 0x0A)

    Jump('loc_378')

    def _loc_32A(): pass

    label('loc_32A')

    OP_D2(0x0027036E, 0x0027037B, 0x0A)

    Jump('loc_378')

    def _loc_337(): pass

    label('loc_337')

    OP_D2(0x00070218, 0x00070224, 0x0A)

    Jump('loc_378')

    def _loc_344(): pass

    label('loc_344')

    OP_D2(0x00070230, 0x0007023C, 0x0A)

    Jump('loc_378')

    def _loc_351(): pass

    label('loc_351')

    OP_D2(0x00070248, 0x00070254, 0x0A)

    Jump('loc_378')

    def _loc_35E(): pass

    label('loc_35E')

    OP_D2(0x00270176, 0x00270183, 0x0A)

    Jump('loc_378')

    def _loc_36B(): pass

    label('loc_36B')

    OP_D2(0x000702B4, 0x000702BB, 0x0A)

    Jump('loc_378')

    def _loc_378(): pass

    label('loc_378')

    Return()

# id: 0x0004 offset: 0x379
@scena.Code('func_04_379')
def func_04_379():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045F, 7, 0x22FF)),
            Expr.Return,
        ),
        'loc_381',
    )

    Return()

    def _loc_381(): pass

    label('loc_381')

    EventBegin(0x00)
    Fade(500)
    OP_6D(2460, 0, -184440, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(65000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 12860, 6000, -184960, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0101, -430, 0, -185160, 90)
    SetChrPos(0x0102, -1300, 0, -184290, 90)
    SetChrPos(0x00F8, -2510, 0, -185420, 90)
    SetChrPos(0x00F9, -2100, 0, -186450, 90)

    @scena.Lambda('lambda_0425')
    def lambda_0425():
        OP_91(0x00FE, 2000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0425)

    @scena.Lambda('lambda_0440')
    def lambda_0440():
        OP_91(0x00FE, 2000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0440)

    @scena.Lambda('lambda_045B')
    def lambda_045B():
        OP_91(0x00FE, 2000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_045B)

    @scena.Lambda('lambda_0476')
    def lambda_0476():
        OP_91(0x00FE, 2000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0476)

    @scena.Lambda('lambda_0491')
    def lambda_0491():
        OP_6D(6460, 0, -184440, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0491)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0008, 4)
    SetChrSubChip(0x0008, 3)

    @scena.Lambda('lambda_04B9')
    def lambda_04B9():
        OP_96(0x00FE, 0x0000229C, 0x00000000, 0xFFFD2D80, 0x00000064, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_04B9)

    OP_22(0x00A3, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 7)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 8)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 9)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 10)
    SetChrSubChip(0x00F9, 0)

    @scena.Lambda('lambda_0579')
    def lambda_0579():
        OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0579)

    WaitForThreadExit(0x0008, 0x0002)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    Sleep(1500)

    TerminateThread(0x0008, 0x00)
    SetChrFlags(0x0008, 0x0020)
    SetChrChipByIndex(0x0008, 6)
    SetChrSubChip(0x0008, 0)

    @scena.Lambda('lambda_05AD')
    def lambda_05AD():
        OP_99(0x00FE, 0x00, 0x02, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05AD)

    WaitForThreadExit(0x0008, 0x0002)

    @scena.Lambda('lambda_05C2')
    def lambda_05C2():
        OP_99(0x00FE, 0x03, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05C2)

    @scena.Lambda('lambda_05D2')
    def lambda_05D2():
        OP_96(0x00FE, 0x000009A6, 0x00000000, 0xFFFD2CB8, 0x000003E8, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05D2)

    OP_22(0x00A3, 0x00, 0x64)
    Sleep(500)

    Battle(0x0000043E, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_615'),
        (0x00000000, 'loc_61A'),
        (0x00000002, 'loc_621'),
        (-1, 'loc_628'),
    )

    def _loc_615(): pass

    label('loc_615')

    OP_B4(0x00)

    Jump('loc_628')

    def _loc_61A(): pass

    label('loc_61A')

    Call(0, 0x0005)

    Jump('loc_628')

    def _loc_621(): pass

    label('loc_621')

    Call(0, 0x0006)

    Jump('loc_628')

    def _loc_628(): pass

    label('loc_628')

    Return()

# id: 0x0005 offset: 0x629
@scena.Code('func_05_629')
def func_05_629():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    SetChrFlags(0x0008, 0x0080)
    OP_6D(1420, 0, -185200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 1420, 0, -185200, 90)
    SetChrPos(0x0001, 1420, 0, -185200, 90)
    SetChrPos(0x0002, 1420, 0, -185200, 90)
    SetChrPos(0x0003, 1420, 0, -185200, 90)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F9, 0)
    OP_A2(0x22FF)
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x704
@scena.Code('func_06_704')
def func_06_704():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    SetChrPos(0x0008, 12860, 6000, -184960, 270)
    ClearChrFlags(0x0008, 0x0080)
    OP_6D(-3750, 0, -185200, 270)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -3750, 0, -185200, 270)
    SetChrPos(0x0001, -3750, 0, -185200, 270)
    SetChrPos(0x0002, -3750, 0, -185200, 270)
    SetChrPos(0x0003, -3750, 0, -185200, 270)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F9, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x7E8
@scena.Code('func_07_7E8')
def func_07_7E8():
    UnlockAchievement(0x02, 0x10, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 1, 0x2309)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C5',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0008, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂粉'], 1)"),
            Expr.Return,
        ),
        'loc_85C',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x2309)

    Jump('loc_8C2')

    def _loc_85C(): pass

    label('loc_85C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0x00000000)

    def _loc_8C2(): pass

    label('loc_8C2')

    Jump('loc_8F6')

    def _loc_8C5(): pass

    label('loc_8C5')

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
    def _loc_8F6(): pass

    label('loc_8F6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x904
@scena.Code('func_08_904')
def func_08_904():
    UnlockAchievement(0x02, 0x11, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0461, 2, 0x230A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E1',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0009, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_978',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x230A)

    Jump('loc_9DE')

    def _loc_978(): pass

    label('loc_978')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0x00000000)

    def _loc_9DE(): pass

    label('loc_9DE')

    Jump('loc_A12')

    def _loc_9E1(): pass

    label('loc_9E1')

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
    def _loc_A12(): pass

    label('loc_A12')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
