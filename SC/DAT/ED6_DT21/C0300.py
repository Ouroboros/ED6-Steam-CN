import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0300.x'
    header.mapIndex       = 19
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00004E20,
            dword_04        = 0x00000000,
            dword_08        = 0x00004268,
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
            word_3A         = 19,
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
        ('ED6_DT29/CH12430._CH', 'ED6_DT29/CH12430P._CP'),
        ('ED6_DT29/CH12431._CH', 'ED6_DT29/CH12431P._CP'),
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT29/CH12400._CH', 'ED6_DT29/CH12400P._CP'),
        ('ED6_DT29/CH12401._CH', 'ED6_DT29/CH12401P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -15740,
            z           = -150,
            y           = -20530,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10000,
            z           = -30,
            y           = 16830,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 11740,
            z           = -290,
            y           = 17440,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 24030,
            z           = -200,
            y           = 33370,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -14010,
            z           = -200,
            y           = 37450,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -15740,
            z           = -150,
            y           = -20530,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10000,
            z           = -30,
            y           = 16830,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0041,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 11740,
            z           = -290,
            y           = 17440,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0042,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 24030,
            z           = -200,
            y           = 33370,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0041,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -14010,
            z           = -200,
            y           = 37450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x202
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x202
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 26850,
            triggerZ            = 60,
            triggerY            = 18280,
            triggerRange        = 1000,
            actorX              = 27590,
            actorZ              = 60,
            actorY              = 18320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x226
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23B',
    )

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x13),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_23B(): pass

    label('loc_23B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 4, 0x1824)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_250',
    )

    MapSetFlags(0x10000000)
    Event(0, func_03_44F)

    def _loc_250(): pass

    label('loc_250')

    Return()

# id: 0x0001 offset: 0x251
@scena.Code('func_01_251')
def func_01_251():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 0, 0x1960)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_263',
    )

    OP_6F(0x0002, 0)

    Jump('loc_26A')

    def _loc_263(): pass

    label('loc_263')

    OP_6F(0x0002, 60)

    def _loc_26A(): pass

    label('loc_26A')

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0011,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2CE',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_2E7')

    def _loc_2CE(): pass

    label('loc_2CE')

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_315',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_315',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)
    OP_C4(0x00, 0x00000004)

    def _loc_315(): pass

    label('loc_315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_325',
    )

    OP_10(0x01, 0x01)
    OP_10(0x02, 0x00)

    Jump('loc_332')

    def _loc_325(): pass

    label('loc_325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Return,
        ),
        'loc_332',
    )

    OP_10(0x01, 0x00)
    OP_10(0x02, 0x01)

    def _loc_332(): pass

    label('loc_332')

    Return()

# id: 0x0002 offset: 0x333
@scena.Code('func_02_333')
def func_02_333():
    UnlockAchievement(0x02, 0x0001, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 0, 0x1960)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_410',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_3A7',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032C, 0, 0x1960))

    Jump('loc_40D')

    def _loc_3A7(): pass

    label('loc_3A7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_40D(): pass

    label('loc_40D')

    Jump('loc_441')

    def _loc_410(): pass

    label('loc_410')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_441(): pass

    label('loc_441')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x44F
@scena.Code('func_03_44F')
def func_03_44F():
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
        'loc_46F',
    )

    Call(0, 0x0004)
    FadeIn(0, 0)
    Call(0, 0x0005)

    def _loc_46F(): pass

    label('loc_46F')

    ChrSetPos(0x0101, -20340, -280, -44000, 0)
    ChrSetPos(0x0103, -19310, -320, -44000, 0)
    ChrSetPos(0x00F8, -19370, -260, -45290, 0)
    ChrSetPos(0x00F9, -20400, -190, -45290, 0)
    CameraMove(-19450, -40, -4470, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(200000, 0)
    OP_6E(463, 0)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    OP_C8(0x0200, 0x0046, 'C_PLAC14._CH', 0x01, 0x03E8)
    ShowPlaceName('神秘森林')
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0537')
    def lambda_0537():
        CameraMove(-20060, -320, -45420, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0537)

    @scena.Lambda('lambda_054F')
    def lambda_054F():
        OP_67(0, 8330, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_054F)

    @scena.Lambda('lambda_0567')
    def lambda_0567():
        CameraSetDistance(3130, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0567)

    @scena.Lambda('lambda_0577')
    def lambda_0577():
        OP_6C(189000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0577)

    OP_6E(262, 8000)

    ChrTalk(
        0x0101,
        (
            '#0010290822V#1002F#6P……这里也完全\n',
            '被浓雾笼罩了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290823V#022F#6P嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290824V这里的视线本来就不好，\n',
            '这下更加寸步难行了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000006, 'loc_63E'),
        (0x00000005, 'loc_67A'),
        (0x00000003, 'loc_6BC'),
        (0x00000004, 'loc_704'),
        (0x00000007, 'loc_740'),
        (-1, 'loc_782'),
    )

    def _loc_63E(): pass

    label('loc_63E')

    ChrTalk(
        0x0107,
        (
            '#0070290825V#065F#5P稍有松懈的话\n',
            '也许就会迷路了呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_782')

    def _loc_67A(): pass

    label('loc_67A')

    ChrTalk(
        0x0106,
        (
            '#0050290826V#051F#5P嘿，掉以轻心的话\n',
            '马上就会迷失方向吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_782')

    def _loc_6BC(): pass

    label('loc_6BC')

    ChrTalk(
        0x0104,
        (
            '#0040290827V#035F#5P呼，要是不集中精力的话，\n',
            '很容易就会迷路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_782')

    def _loc_704(): pass

    label('loc_704')

    ChrTalk(
        0x0105,
        (
            '#0060290828V#043F#5P稍微一不注意\n',
            '就会迷失方向了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_782')

    def _loc_740(): pass

    label('loc_740')

    ChrTalk(
        0x0108,
        (
            '#0080290829V#074F#5P如果放松精神的话，\n',
            '很容易就会迷路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_782')

    def _loc_782(): pass

    label('loc_782')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000006, 'loc_79F'),
        (0x00000005, 'loc_7DF'),
        (0x00000003, 'loc_81F'),
        (0x00000004, 'loc_85F'),
        (0x00000007, 'loc_89F'),
        (-1, 'loc_8DF'),
    )

    def _loc_79F(): pass

    label('loc_79F')

    ChrTalk(
        0x0107,
        (
            '#0070290830V#062F#5P看来最好还是\n',
            '仔细看着指南针前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DF')

    def _loc_7DF(): pass

    label('loc_7DF')

    ChrTalk(
        0x0106,
        (
            '#0050290831V#555F#5P看来最好还是\n',
            '仔细看着指南针前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DF')

    def _loc_81F(): pass

    label('loc_81F')

    ChrTalk(
        0x0104,
        (
            '#0040290832V#030F#5P看来最好还是\n',
            '仔细看着指南针前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DF')

    def _loc_85F(): pass

    label('loc_85F')

    ChrTalk(
        0x0105,
        (
            '#0060290833V#042F#5P看来最好还是\n',
            '仔细看着指南针前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DF')

    def _loc_89F(): pass

    label('loc_89F')

    ChrTalk(
        0x0108,
        (
            '#0080290834V#072F#5P看来最好还是\n',
            '仔细看着指南针前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8DF')

    def _loc_8DF(): pass

    label('loc_8DF')

    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    SetScenaFlags(ScenaFlag(0x0304, 4, 0x1824))
    OP_28(0x0092, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x904
@scena.Code('func_04_904')
def func_04_904():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_981'),
        (0x00000001, 'loc_987'),
        (-1, 'loc_98D'),
    )

    def _loc_981(): pass

    label('loc_981')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_98D')

    def _loc_987(): pass

    label('loc_987')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_98D')

    def _loc_98D(): pass

    label('loc_98D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_99B',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_99F')

    def _loc_99B(): pass

    label('loc_99B')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_99F(): pass

    label('loc_99F')

    Return()

# id: 0x0005 offset: 0x9A0
@scena.Code('func_05_9A0')
def func_05_9A0():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
