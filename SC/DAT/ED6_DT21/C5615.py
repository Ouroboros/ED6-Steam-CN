import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5615_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5615   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5615.x'
    header.mapIndex       = 1
    header.bgm            = 61
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
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT26/CH20406._CH', 'ED6_DT26/CH20406P._CP'),
        ('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP'),
        ('ED6_DT27/CH03084._CH', 'ED6_DT27/CH03084P._CP'),
        ('ED6_DT26/CH20373._CH', 'ED6_DT26/CH20373P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
    ]

# id: 0x10001 offset: 0x182
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '哨兵235',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵235',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵570',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵570',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x222
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x222
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -157870,
            triggerZ            = 0,
            triggerY            = 100,
            triggerRange        = 800,
            actorX              = -157870,
            actorZ              = 1000,
            actorY              = 100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x246
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 5, 0x1C0D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25E',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25E',
    )

    Event(0, func_03_27F)

    def _loc_25E(): pass

    label('loc_25E')

    Return()

# id: 0x0001 offset: 0x25F
@scena.Code('func_01_25F')
def func_01_25F():
    OP_74(0x0000, 0x00000000, 0x0000)

    Return()

# id: 0x0002 offset: 0x269
@scena.Code('func_02_269')
def func_02_269():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_27E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_269')

    def _loc_27E(): pass

    label('loc_27E')

    Return()

# id: 0x0003 offset: 0x27F
@scena.Code('func_03_27F')
def func_03_27F():
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
        'loc_296',
    )

    Call(0, 0x000C)
    Call(0, 0x000D)

    def _loc_296(): pass

    label('loc_296')

    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0008, -153870, 0, -30, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0109, -143220, 10, 460, 270)
    ChrSetPos(0x0101, -143310, 10, -640, 270)
    ChrSetPos(0x00F8, -142050, 0, 460, 270)
    ChrSetPos(0x00F9, -142050, 0, -640, 270)
    CameraMove(-142530, 0, 0, 0)
    OP_67(0, 7700, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(315000, 0)
    OP_6E(265, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321287V#1002F#6P……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_036D')
    def lambda_036D():
        CameraMove(-151430, 0, 550, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_036D)

    @scena.Lambda('lambda_0385')
    def lambda_0385():
        OP_67(0, 5420, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_0385)

    @scena.Lambda('lambda_039D')
    def lambda_039D():
        CameraSetDistance(1950, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_039D)

    @scena.Lambda('lambda_03AD')
    def lambda_03AD():
        OP_6E(404, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03AD)

    Sleep(2000)

    ChrSetDirection(0x0008, 90, 400)
    Sleep(200)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 20)
    ChrSetSubChip(0x0008, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0120321288V#1313F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0109, 15)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_43F'),
        (0x00000005, 'loc_447'),
        (0x00000003, 'loc_44F'),
        (0x00000004, 'loc_457'),
        (0x00000006, 'loc_45F'),
        (0x00000007, 'loc_467'),
        (-1, 'loc_46F'),
    )

    def _loc_43F(): pass

    label('loc_43F')

    ChrSetChipByIndex(0x00F8, 3)

    Jump('loc_46F')

    def _loc_447(): pass

    label('loc_447')

    ChrSetChipByIndex(0x00F8, 5)

    Jump('loc_46F')

    def _loc_44F(): pass

    label('loc_44F')

    ChrSetChipByIndex(0x00F8, 7)

    Jump('loc_46F')

    def _loc_457(): pass

    label('loc_457')

    ChrSetChipByIndex(0x00F8, 9)

    Jump('loc_46F')

    def _loc_45F(): pass

    label('loc_45F')

    ChrSetChipByIndex(0x00F8, 11)

    Jump('loc_46F')

    def _loc_467(): pass

    label('loc_467')

    ChrSetChipByIndex(0x00F8, 13)

    Jump('loc_46F')

    def _loc_46F(): pass

    label('loc_46F')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_490'),
        (0x00000005, 'loc_498'),
        (0x00000003, 'loc_4A0'),
        (0x00000004, 'loc_4A8'),
        (0x00000006, 'loc_4B0'),
        (0x00000007, 'loc_4B8'),
        (-1, 'loc_4C0'),
    )

    def _loc_490(): pass

    label('loc_490')

    ChrSetChipByIndex(0x00F9, 3)

    Jump('loc_4C0')

    def _loc_498(): pass

    label('loc_498')

    ChrSetChipByIndex(0x00F9, 5)

    Jump('loc_4C0')

    def _loc_4A0(): pass

    label('loc_4A0')

    ChrSetChipByIndex(0x00F9, 7)

    Jump('loc_4C0')

    def _loc_4A8(): pass

    label('loc_4A8')

    ChrSetChipByIndex(0x00F9, 9)

    Jump('loc_4C0')

    def _loc_4B0(): pass

    label('loc_4B0')

    ChrSetChipByIndex(0x00F9, 11)

    Jump('loc_4C0')

    def _loc_4B8(): pass

    label('loc_4B8')

    ChrSetChipByIndex(0x00F9, 13)

    Jump('loc_4C0')

    def _loc_4C0(): pass

    label('loc_4C0')

    @scena.Lambda('lambda_04C6')
    def lambda_04C6():
        ChrMoveToRelativeAsync(0x00FE, -4300, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04C6)

    Sleep(60)

    @scena.Lambda('lambda_04E6')
    def lambda_04E6():
        ChrMoveToRelativeAsync(0x00FE, -4300, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_04E6)

    Sleep(100)

    @scena.Lambda('lambda_0506')
    def lambda_0506():
        ChrMoveToRelativeAsync(0x00FE, -4200, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0506)

    Sleep(70)

    @scena.Lambda('lambda_0526')
    def lambda_0526():
        ChrMoveToRelativeAsync(0x00FE, -4200, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0526)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010321289V#1002F#6P果然亚妮拉丝也……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321290V#1069F#4P总之只能\n',
            '先将她压制住了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    CreateThread(0x0009, 0x00, 0x00, func_04_662)
    Sleep(200)

    CreateThread(0x000A, 0x00, 0x00, func_05_6C0)
    Sleep(200)

    CreateThread(0x000B, 0x00, 0x00, func_06_71E)
    Sleep(200)

    CreateThread(0x000C, 0x00, 0x00, func_07_77C)
    Sleep(1500)

    @scena.Lambda('lambda_05DE')
    def lambda_05DE():
        CameraMove(-151500, 0, 500, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05DE)

    @scena.Lambda('lambda_05F6')
    def lambda_05F6():
        CameraSetDistance(1760, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_05F6)

    CreateThread(0x0101, 0x00, 0x00, func_08_7DA)
    CreateThread(0x0008, 0x00, 0x00, func_09_911)
    Sleep(300)

    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0109, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x00000420, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_658'),
        (-1, 'loc_65D'),
    )

    def _loc_658(): pass

    label('loc_658')

    OP_B4(0x00)

    Jump('loc_65D')

    def _loc_65D(): pass

    label('loc_65D')

    Call(0, 0x000A)

    Return()

# id: 0x0004 offset: 0x662
@scena.Code('func_04_662')
def func_04_662():
    CreateThread(0x00FE, 0x03, 0x00, func_02_269)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -154580, 1200, 1920, 90)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_069F')
    def lambda_069F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_069F)

    ChrMoveTo(0x00FE, -154580, 0, 1920, 2000, 0x00)

    Return()

# id: 0x0005 offset: 0x6C0
@scena.Code('func_05_6C0')
def func_05_6C0():
    CreateThread(0x00FE, 0x03, 0x00, func_02_269)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -154600, 1200, -1460, 90)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_06FD')
    def lambda_06FD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_06FD)

    ChrMoveTo(0x00FE, -154600, 0, -1460, 2000, 0x00)

    Return()

# id: 0x0006 offset: 0x71E
@scena.Code('func_06_71E')
def func_06_71E():
    CreateThread(0x00FE, 0x03, 0x00, func_02_269)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -156040, 1200, 1040, 90)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_075B')
    def lambda_075B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_075B)

    ChrMoveTo(0x00FE, -156040, 0, 1040, 2000, 0x00)

    Return()

# id: 0x0007 offset: 0x77C
@scena.Code('func_07_77C')
def func_07_77C():
    CreateThread(0x00FE, 0x03, 0x00, func_02_269)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -156170, 1210, -750, 90)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_07B9')
    def lambda_07B9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_07B9)

    ChrMoveTo(0x00FE, -156170, 0, -750, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0x7DA
@scena.Code('func_08_7DA')
def func_08_7DA():
    ChrSetChipByIndex(0x0101, 2)
    ChrSetChipByIndex(0x0109, 16)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_805'),
        (0x00000005, 'loc_80D'),
        (0x00000003, 'loc_815'),
        (0x00000004, 'loc_81D'),
        (0x00000006, 'loc_825'),
        (0x00000007, 'loc_82D'),
        (-1, 'loc_835'),
    )

    def _loc_805(): pass

    label('loc_805')

    ChrSetChipByIndex(0x00F8, 4)

    Jump('loc_835')

    def _loc_80D(): pass

    label('loc_80D')

    ChrSetChipByIndex(0x00F8, 6)

    Jump('loc_835')

    def _loc_815(): pass

    label('loc_815')

    ChrSetChipByIndex(0x00F8, 8)

    Jump('loc_835')

    def _loc_81D(): pass

    label('loc_81D')

    ChrSetChipByIndex(0x00F8, 10)

    Jump('loc_835')

    def _loc_825(): pass

    label('loc_825')

    ChrSetChipByIndex(0x00F8, 12)

    Jump('loc_835')

    def _loc_82D(): pass

    label('loc_82D')

    ChrSetChipByIndex(0x00F8, 14)

    Jump('loc_835')

    def _loc_835(): pass

    label('loc_835')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_856'),
        (0x00000005, 'loc_85E'),
        (0x00000003, 'loc_866'),
        (0x00000004, 'loc_86E'),
        (0x00000006, 'loc_876'),
        (0x00000007, 'loc_87E'),
        (-1, 'loc_886'),
    )

    def _loc_856(): pass

    label('loc_856')

    ChrSetChipByIndex(0x00F9, 4)

    Jump('loc_886')

    def _loc_85E(): pass

    label('loc_85E')

    ChrSetChipByIndex(0x00F9, 6)

    Jump('loc_886')

    def _loc_866(): pass

    label('loc_866')

    ChrSetChipByIndex(0x00F9, 8)

    Jump('loc_886')

    def _loc_86E(): pass

    label('loc_86E')

    ChrSetChipByIndex(0x00F9, 10)

    Jump('loc_886')

    def _loc_876(): pass

    label('loc_876')

    ChrSetChipByIndex(0x00F9, 12)

    Jump('loc_886')

    def _loc_87E(): pass

    label('loc_87E')

    ChrSetChipByIndex(0x00F9, 14)

    Jump('loc_886')

    def _loc_886(): pass

    label('loc_886')

    ChrSetFlags(0x00F8, 0x1000)
    ChrSetFlags(0x00F9, 0x1000)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0109, 0x1000)

    @scena.Lambda('lambda_08A0')
    def lambda_08A0():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08A0)

    Sleep(50)

    @scena.Lambda('lambda_08C0')
    def lambda_08C0():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_08C0)

    @scena.Lambda('lambda_08DB')
    def lambda_08DB():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_08DB)

    Sleep(50)

    @scena.Lambda('lambda_08FB')
    def lambda_08FB():
        ChrMoveToRelativeAsync(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_08FB)

    Return()

# id: 0x0009 offset: 0x911
@scena.Code('func_09_911')
def func_09_911():
    ChrSetChipByIndex(0x0008, 17)

    @scena.Lambda('lambda_091C')
    def lambda_091C():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_091C)

    ChrSetChipByIndex(0x0009, 24)

    @scena.Lambda('lambda_093C')
    def lambda_093C():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_093C)

    Sleep(50)

    ChrSetChipByIndex(0x000A, 24)

    @scena.Lambda('lambda_0961')
    def lambda_0961():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0961)

    ChrSetChipByIndex(0x000B, 26)

    @scena.Lambda('lambda_0981')
    def lambda_0981():
        ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0981)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 26)

    @scena.Lambda('lambda_09A6')
    def lambda_09A6():
        ChrMoveToRelativeAsync(0x00FE, 3500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_09A6)

    Return()

# id: 0x000A offset: 0x9BC
@scena.Code('func_0A_9BC')
def func_0A_9BC():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0109, 15)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0109, 65535)
    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    ChrSetPos(0x0008, -153000, 0, -70, 90)
    ChrSetChipByIndex(0x0008, 19)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0109, -150930, 20, 460, 270)
    ChrSetPos(0x0101, -150850, 20, -840, 270)
    ChrSetPos(0x00F8, -149630, 20, 460, 270)
    ChrSetPos(0x00F9, -149540, 20, -840, 270)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0109, 0x1000)
    ChrClearFlags(0x00F8, 0x1000)
    ChrClearFlags(0x00F9, 0x1000)
    CameraMove(-152380, 20, 1000, 0)
    OP_67(0, 5500, -10000, 0)
    CameraSetDistance(1920, 0)
    OP_6C(315000, 0)
    OP_6E(393, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321291V#1007F#6P亚、亚妮拉丝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321292V#1019F好像变得\n',
            '相当强的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BC1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321293V#524F#4P嗯，为了不输给你，\n',
            '一直在努力修练吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321294V#1025F#6P是嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D33')

    def _loc_BC1(): pass

    label('loc_BC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C3A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321295V#051F#4P嗯，为了不输给你，\n',
            '一直在努力修练吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321296V#1025F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D33')

    def _loc_C3A(): pass

    label('loc_C3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CB7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321297V#524F#4P嗯，为了不输给你，\n',
            '一直在努力修练的样子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321298V#1025F#6P是嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D33')

    def _loc_CB7(): pass

    label('loc_CB7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D33',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321299V#051F#4P嗯，为了不输给你，\n',
            '一直在努力修练的样子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321300V#1025F#6P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D33(): pass

    label('loc_D33')

    ChrTalk(
        0x0109,
        (
            '#0180321301V#1060F#4P好……\n',
            '来把她唤醒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D69')
    def lambda_0D69():
        CameraMove(-153380, 20, 1000, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_0D69)

    ChrMoveTo(0x0109, -151800, 0, -30, 1500, 0x00)
    ChrSetDirection(0x0109, 270, 400)
    WaitForThreadExit(0x0109, 0x0001)
    Fade(500)
    ChrSetChipByIndex(0x0109, 22)
    ChrSetSubChip(0x0109, 0)
    Sleep(500)

    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0109, 1)
    Sleep(1000)

    LoadEffect(0x00, 'scraft\\\\sc008_02.eff')
    PlayEffect(0x00, 0xFF, 0x0109, 0, 1100, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    LoadEffect(0x00, 'scraft\\\\sc001_05.eff')
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    OP_9E(0x0008, 20, 0, 500, 3000)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0120321302V#1312F#5P啊呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_99(0x0008, 0x00, 0x03, 1500)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_F49',
    )

    ChrTalk(
        0x0008,
        (
            '#0120321303V#1314F#5P嘿嘿……\n',
            '艾丝蒂尔……前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321304V还有凯文先生也……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321305V真的很谢谢\n',
            '你们来救我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FBF')

    def _loc_F49(): pass

    label('loc_F49')

    ChrTalk(
        0x0008,
        (
            '#0120321306V#1314F#5P嘿嘿……艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321304V还有凯文先生也……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321305V真的很谢谢\n',
            '你们来救我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FBF(): pass

    label('loc_FBF')

    Sleep(100)

    Fade(500)
    ChrSetChipByIndex(0x0109, 65535)
    OP_0D()

    @scena.Lambda('lambda_0FD5')
    def lambda_0FD5():
        ChrMoveTo(0x0109, -150930, 20, 460, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_0FD5)

    ChrTalk(
        0x0101,
        (
            '#0010321309V#1025F#6P亚妮拉丝……\n',
            '身体不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321310V#1311F#5P嗯、嗯……\n',
            '……没有问题哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321311V#812F话说回来……\n',
            '卡露娜前辈他们……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10EB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321312V#021F#4P别担心，全员都救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321313V你是最后一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A7')

    def _loc_10EB(): pass

    label('loc_10EB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_114A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321314V#051F#4P别担心，全员都救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050321315V你是最后一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A7')

    def _loc_114A(): pass

    label('loc_114A')

    ChrTalk(
        0x0109,
        (
            '#0180321316V#1062F#4P别担心，全员都救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321317V#1061F亚妮拉丝是最后一个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A7(): pass

    label('loc_11A7')

    ChrTalk(
        0x0008,
        (
            '#0120321318V#1314F#5P是、是吗……\n',
            '太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321319V#1316F对不起哦，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321320V难得约定要好一起战斗，\n',
            '却变成这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_135B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321321V#1006F#6P不，别放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321322V都是多亏了亚妮拉丝你们，\n',
            '我们才会知道这个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030321323V#021F#4P你们已经充分地\n',
            '完成了自己的工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050321324V#051F#4P之后就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321325V#1314F#5P艾丝蒂尔……\n',
            '……前辈们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1650')

    def _loc_135B(): pass

    label('loc_135B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1470',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321326V#1006F#6P不，别放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321322V都是多亏了亚妮拉丝你们，\n',
            '我们才会知道这个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030321328V#021F#4P你们已经充分地\n',
            '完成了自己的工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321329V#020F之后就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321330V#1314F#5P艾丝蒂尔……\n',
            '……雪拉前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1650')

    def _loc_1470(): pass

    label('loc_1470')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1582',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321331V#1006F#6P不，别放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321322V都是多亏了亚妮拉丝你们，\n',
            '我们才会知道这个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050321333V#051F#4P你们已经充分地\n',
            '完成了自己的工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050321334V之后就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321335V#1314F#5P艾丝蒂尔……\n',
            '……阿加特前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1650')

    def _loc_1582(): pass

    label('loc_1582')

    ChrTalk(
        0x0101,
        (
            '#0010321336V#1006F#4P哪里，别放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321337V都是多亏了亚妮拉丝你们，\n',
            '我们才会知道这个地方的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321338V我认为你们已经充分地\n',
            '完成了探索据点的工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321339V#1314F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1650(): pass

    label('loc_1650')

    OP_62(0x0008, 0x0000012C, 1300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0120321340V#1317F#5P对、对了艾丝蒂尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321341V我……有件事\n',
            '必须告诉你才行……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321342V#1004F#6P咦……什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321343V#1317F#5P那个……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321344V在、在逃跑的过程中，\n',
            '我看见约修亚了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321345V#1020F#6P#5S！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17D5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321346V#023F#4P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D5(): pass

    label('loc_17D5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1809',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321347V#052F#4P你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1809(): pass

    label('loc_1809')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1839',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321348V#043F#4P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1839(): pass

    label('loc_1839')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_186D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321349V#065F#4P哥、哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_186D(): pass

    label('loc_186D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18A3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321350V#073F#4P……那家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A3(): pass

    label('loc_18A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18D1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321351V#032F#4P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18D1(): pass

    label('loc_18D1')

    ChrTalk(
        0x0008,
        (
            '#0120321352V#813F#5P我在被士兵逼到无路可退时，\n',
            '他就突然现身并破坏了包围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321353V那身衣服和黑发我有印象，\n',
            '应该不会错的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321354V#1026F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321355V#1317F#5P艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321356V#1016F#6P──啊。\n',
            '嗯，抱歉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321357V#1005F那、那么亚妮拉丝！\n',
            '约修亚去了哪里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321358V#813F#5P不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321359V我当时也只顾着逃跑，\n',
            '结果还是被抓住了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321360V#812F但是……或许是\n',
            '去了屋顶也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321361V#1020F#6P屋顶？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321362V#812F#5P这座建筑物……屋顶好像有\n',
            '飞艇的起降场……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321363V这里的士兵和研究员\n',
            '好像都到那边去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321364V#1002F#6P是吗……明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321365V#1063F#4P亚妮拉丝。\n',
            '你一个人可以逃出去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120321366V#816F#5P嗯……没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 20, 0, 300, 3000)
    OP_99(0x0008, 0x03, 0x00, 1000)
    Fade(500)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0120321367V#817F#5P这前面……\n',
            '说不定还有什么埋伏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120321368V#812F大家……\n',
            '要多加小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C6F')
    def lambda_1C6F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1C6F')

    DispatchAsync2(0x0101, 0x0001, lambda_1C6F)

    @scena.Lambda('lambda_1C80')
    def lambda_1C80():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1C80')

    DispatchAsync2(0x0109, 0x0001, lambda_1C80)

    @scena.Lambda('lambda_1C91')
    def lambda_1C91():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1C91')

    DispatchAsync2(0x00F8, 0x0001, lambda_1C91)

    @scena.Lambda('lambda_1CA2')
    def lambda_1CA2():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_1CA2')

    DispatchAsync2(0x00F9, 0x0001, lambda_1CA2)

    @scena.Lambda('lambda_1CB3')
    def lambda_1CB3():
        CameraMove(-144770, 0, -460, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1CB3)

    ChrWalkTo(0x0008, -151030, 20, -2580, 2000, 0x00)

    @scena.Lambda('lambda_1CDF')
    def lambda_1CDF():
        OP_9E(0x00FE, 20, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1CDF)

    ChrWalkTo(0x0008, -147340, 20, -2830, 2500, 0x00)

    @scena.Lambda('lambda_1D0D')
    def lambda_1D0D():
        OP_9E(0x00FE, 20, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D0D)

    ChrWalkTo(0x0008, -143720, 10, -510, 2000, 0x00)

    @scena.Lambda('lambda_1D3B')
    def lambda_1D3B():
        OP_9E(0x00FE, 20, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D3B)

    ChrWalkTo(0x0008, -140470, 10, -160, 2500, 0x00)

    @scena.Lambda('lambda_1D69')
    def lambda_1D69():
        ChrWalkTo(0x00FE, -139070, 10, -160, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D69)

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 400)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_1DAE')
    def lambda_1DAE():
        CameraMove(-150730, 20, 50, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DAE)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010321369V#1026F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321370V#1065F#5P没想到，约修亚\n',
            '竟然会来到这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321371V#1063F总之快前往屋顶吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321372V#1002F#5P……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0381, 5, 0x1C0D))
    OP_28(0x0098, 0x01, 0x0100)
    OP_28(0x0098, 0x01, 0x0200)
    OP_28(0x0098, 0x01, 0x0400)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x1E95
@scena.Code('func_0B_1E95')
def func_0B_1E95():
    EventBegin(0x00)
    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    OP_74(0x0000, 0x00000000, 0x0003)
    SetMessageWindowPos(-1, -1, 24, 5)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『关于β』\n',
            ' \n',
            '以利贝尔各地进行的实验结果为基础，\n',
            '『β』的调整终于进入了最后的阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_74(0x0000, 0x00000000, 0x0001)
    SetMessageWindowPos(-1, -1, 24, 5)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S这是完全模仿\n',
            '原来机能的仿真器，\n',
            '导力场的同步率也超过９０％。\n',
            '就结果来说，尺寸虽然扩大了，\n',
            '但要完成『福音计划』……（※以下删除）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 6, 0x1C0E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2013',
    )

    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['蓝色密码卡']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['蓝色密码卡'], 1)
    Sleep(500)

    def _loc_2013(): pass

    label('loc_2013')

    SetScenaFlags(ScenaFlag(0x0381, 6, 0x1C0E))
    OP_28(0x0098, 0x01, 0x0800)
    OP_74(0x0000, 0x00000000, 0x0000)
    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    EventEnd(0x01)

    Return()

# id: 0x000C offset: 0x2032
@scena.Code('func_0C_2032')
def func_0C_2032():
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
        (0x00000000, 'loc_20AF'),
        (0x00000001, 'loc_20B5'),
        (-1, 'loc_20BB'),
    )

    def _loc_20AF(): pass

    label('loc_20AF')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_20BB')

    def _loc_20B5(): pass

    label('loc_20B5')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_20BB')

    def _loc_20BB(): pass

    label('loc_20BB')

    Return()

# id: 0x000D offset: 0x20BC
@scena.Code('func_0D_20BC')
def func_0D_20BC():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['凯文神父'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
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
