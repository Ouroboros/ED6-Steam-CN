import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4202   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4202.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x849
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 43860,
            z                   = 1500,
            y                   = -5600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 13590,
            z           = 0,
            y           = 67390,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13650,
            z           = 0,
            y           = 73480,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13600,
            z           = 0,
            y           = 79600,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13660,
            z           = 0,
            y           = 83670,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13620,
            z           = 0,
            y           = 90730,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 60960,
            z           = 0,
            y           = 94820,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 100830,
            z           = 0,
            y           = 20580,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 38210,
            z           = 0,
            y           = -520,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0274,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15760,
            z           = 0,
            y           = -10320,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0274,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34200,
            z           = 0,
            y           = 7700,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0274,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 30560,
            z           = 0,
            y           = -65610,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0274,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x27E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x27E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 43930,
            triggerZ            = 0,
            triggerY            = -6210,
            triggerRange        = 1000,
            actorX              = 43860,
            actorZ              = 1500,
            actorY              = -5600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41920,
            triggerZ            = 450,
            triggerY            = 124030,
            triggerRange        = 1000,
            actorX              = 41950,
            actorZ              = 1950,
            actorY              = 123110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 29340,
            triggerZ            = 0,
            triggerY            = 130710,
            triggerRange        = 1000,
            actorX              = 28570,
            actorZ              = 1500,
            actorY              = 130759,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40750,
            triggerZ            = 0,
            triggerY            = 60500,
            triggerRange        = 1000,
            actorX              = 41500,
            actorZ              = -1000,
            actorY              = 55500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x30E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x30F
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 2, 0x171A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_321',
    )

    OP_6F(0x0000, 0)

    Jump('loc_328')

    def _loc_321(): pass

    label('loc_321')

    OP_6F(0x0000, 60)

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 4, 0x171C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33A',
    )

    OP_6F(0x0001, 0)

    Jump('loc_341')

    def _loc_33A(): pass

    label('loc_33A')

    OP_6F(0x0001, 60)

    def _loc_341(): pass

    label('loc_341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 6, 0x171E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_353',
    )

    OP_6F(0x0002, 0)

    Jump('loc_35A')

    def _loc_353(): pass

    label('loc_353')

    OP_6F(0x0002, 60)

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_36F',
    )

    OP_10(0x15, 0x00)
    OP_10(0x16, 0x01)

    Jump('loc_375')

    def _loc_36F(): pass

    label('loc_36F')

    OP_10(0x15, 0x01)
    OP_10(0x16, 0x00)

    def _loc_375(): pass

    label('loc_375')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x37B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_390',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_390(): pass

    label('loc_390')

    Return()

# id: 0x0003 offset: 0x391
@scena.Code('func_03_391')
def func_03_391():
    UnlockAchievement(0x02, 0x04, 0x02, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 2, 0x171A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_529',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 3, 0x171B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_475',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_03E8')
    def lambda_03E8():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03E8)

    @scena.Lambda('lambda_0403')
    def lambda_0403():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0403)

    ClearChrFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000276, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_450'),
        (0x00000002, 'loc_462'),
        (0x00000001, 'loc_472'),
        (-1, 'loc_475'),
    )

    def _loc_450(): pass

    label('loc_450')

    OP_A2(0x171B)
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_475')

    def _loc_462(): pass

    label('loc_462')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_472(): pass

    label('loc_472')

    OP_B4(0x00)

    Return()

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['水晶高跟鞋'], 1)"),
            Expr.Return,
        ),
        'loc_4C4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['水晶高跟鞋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x171A)

    Jump('loc_526')

    def _loc_4C4(): pass

    label('loc_4C4')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['水晶高跟鞋']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['水晶高跟鞋']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_526(): pass

    label('loc_526')

    Jump('loc_558')

    def _loc_529(): pass

    label('loc_529')

    FadeOut(300, 0, 100)

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
    def _loc_558(): pass

    label('loc_558')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x566
@scena.Code('func_04_566')
def func_04_566():
    UnlockAchievement(0x02, 0x04, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 4, 0x171C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E4',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000001E)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x01, 0x00C8)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x171C)

    Jump('loc_5FE')

    def _loc_5E4(): pass

    label('loc_5E4')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5FE(): pass

    label('loc_5FE')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x610
@scena.Code('func_05_610')
def func_05_610():
    UnlockAchievement(0x02, 0x05, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 6, 0x171E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6ED',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['红虫'], 1)"),
            Expr.Return,
        ),
        'loc_684',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['红虫']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x171E)

    Jump('loc_6EA')

    def _loc_684(): pass

    label('loc_684')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['红虫']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['红虫']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_6EA(): pass

    label('loc_6EA')

    Jump('loc_71E')

    def _loc_6ED(): pass

    label('loc_6ED')

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
    def _loc_71E(): pass

    label('loc_71E')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x72C
@scena.Code('func_06_72C')
def func_06_72C():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0764')
    def lambda_0764():
        OP_6D(40170, 0, 57370, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0764)

    @scena.Lambda('lambda_077C')
    def lambda_077C():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_077C)

    @scena.Lambda('lambda_0794')
    def lambda_0794():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0794)

    @scena.Lambda('lambda_07A4')
    def lambda_07A4():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_07A4)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
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
    OP_56(0x00)
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82B',
    )

    OP_C0(0x0E, 0x00000029, 0x00009F7E, 0x00000000, 0x0000EC54, 0x000000B4, 0x00009CD6, 0xFFFFFE0C, 0x0000D73C)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_83A')

    def _loc_82B(): pass

    label('loc_82B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83A',
    )

    EventEnd(0x01)

    def _loc_83A(): pass

    label('loc_83A')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
