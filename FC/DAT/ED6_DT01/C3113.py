import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3113   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '吉尔'),
    TXT(0x03, '多伦'),
    TXT(0x04, '士兵的声音'),
    TXT(0x05, '男性的声音'),
    TXT(0x06, '空贼'),
    TXT(0x07, '空贼'),
    TXT(0x08, '空贼'),
    TXT(0x09, '空贼'),
    TXT(0x0A, '空贼'),
    TXT(0x0B, '空贼'),
    TXT(0x0C, '亲卫队'),
    TXT(0x0D, '亲卫队'),
    TXT(0x0E, '亲卫队'),
    TXT(0x0F, '戴尔蒙市长'),
    TXT(0x10, '基尔巴特'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3113.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1DB2
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
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02420._CH', 'ED6_DT07/CH02420P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -142470,
            z                   = 0,
            y                   = -550,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -142390,
            z                   = 0,
            y                   = 4030,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -140430,
            z                   = 0,
            y                   = 4030,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -8770,
            z                   = 0,
            y                   = -4840,
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
            x                   = 18140,
            z                   = 0,
            y                   = -490,
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
            x                   = -132720,
            z                   = 0,
            y                   = 1930,
            direction           = 171,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -131510,
            z                   = 0,
            y                   = 2890,
            direction           = 167,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -130850,
            z                   = 0,
            y                   = 1430,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -124600,
            z                   = 0,
            y                   = 2120,
            direction           = 154,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -123080,
            z                   = 0,
            y                   = 2980,
            direction           = 177,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -123420,
            z                   = 0,
            y                   = 950,
            direction           = 189,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -110610,
            z                   = 0,
            y                   = 3930,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -108510,
            z                   = 0,
            y                   = 3910,
            direction           = 179,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -106630,
            z                   = 0,
            y                   = 3280,
            direction           = 240,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -119400,
            z                   = 0,
            y                   = 4390,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -115010,
            z                   = 0,
            y                   = -550,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2E2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 20980,
            triggerZ            = 0,
            triggerY            = 158210,
            triggerRange        = 800,
            actorX              = 20980,
            actorZ              = 1000,
            actorY              = 158210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14930,
            triggerZ            = 0,
            triggerY            = 1930,
            triggerRange        = 800,
            actorX              = -14930,
            actorZ              = 1000,
            actorY              = 1930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2910,
            triggerZ            = 0,
            triggerY            = 1930,
            triggerRange        = 800,
            actorX              = -2910,
            actorZ              = 1000,
            actorY              = 1930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7070,
            triggerZ            = 0,
            triggerY            = 1930,
            triggerRange        = 800,
            actorX              = 7070,
            actorZ              = 1000,
            actorY              = 1930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23900,
            triggerZ            = 0,
            triggerY            = 114940,
            triggerRange        = 800,
            actorX              = 23900,
            actorZ              = 1000,
            actorY              = 114940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23900,
            triggerZ            = 0,
            triggerY            = 126940,
            triggerRange        = 800,
            actorX              = 23900,
            actorZ              = 1000,
            actorY              = 126940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23900,
            triggerZ            = 0,
            triggerY            = 138940,
            triggerRange        = 800,
            actorX              = 23900,
            actorZ              = 1000,
            actorY              = 138940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3DE
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_3EE'),
        (0x00000068, 'loc_404'),
        (-1, 'loc_41A'),
    )

    def _loc_3EE(): pass

    label('loc_3EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 4, 0x56C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_401',
    )

    SetScenaFlags(ScenaFlag(0x00AD, 4, 0x56C))
    Event(0, 0x0003)

    def _loc_401(): pass

    label('loc_401')

    Jump('loc_41A')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 6, 0x56E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 5, 0x56D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_417',
    )

    SetScenaFlags(ScenaFlag(0x00AD, 6, 0x56E))
    Event(0, 0x0010)

    def _loc_417(): pass

    label('loc_417')

    Jump('loc_41A')

    def _loc_41A(): pass

    label('loc_41A')

    Return()

# id: 0x0001 offset: 0x41B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 4, 0x56C)),
            Expr.Return,
        ),
        'loc_427',
    )

    OP_1B(0x01, 0x00, 0x000E)

    def _loc_427(): pass

    label('loc_427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 4, 0x56C)),
            Expr.Return,
        ),
        'loc_433',
    )

    OP_1B(0x00, 0x00, 0x000F)

    def _loc_433(): pass

    label('loc_433')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 7, 0x56F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_443',
    )

    OP_72(0x0012, 0x0010)

    Jump('loc_447')

    def _loc_443(): pass

    label('loc_443')

    OP_64(0x00, 0x0001)

    def _loc_447(): pass

    label('loc_447')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Return,
        ),
        'loc_453',
    )

    PlaySE(172, 0x01, 0x50)

    def _loc_453(): pass

    label('loc_453')

    Return()

# id: 0x0002 offset: 0x454
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_469',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_469(): pass

    label('loc_469')

    Return()

# id: 0x0003 offset: 0x46A
@scena.Code('func_03_46A')
def func_03_46A():
    EventBegin(0x00)
    OP_24(0x00AC, 0x3C)
    CameraMove(-98070, 0, 2550, 0)
    OP_67(0, 8870, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -150200, 3000, 3950, 90)
    SetChrPos(0x0102, -150200, 3000, 3950, 90)
    SetChrPos(0x0106, -150200, 3000, 3950, 90)
    SetChrPos(0x0107, -150200, 3000, 3950, 90)
    SetChrPos(0x010B, -150200, 3000, 3950, 90)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0511')
    def lambda_0511():
        CameraMove(-142510, 0, 2940, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0511)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    CameraMove(-142510, 0, 2940, 0)
    OP_67(0, 6470, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0090091196V#215F#1P我、我说……\n',
            '总觉得外面好像很吵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290091197V#200F啊……\n',
            '好像有入侵者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300091198V#192F啥，有入侵者……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300091199V#196F呆不下去了！\n',
            '趁此机会逃狱吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290091200V#203F大哥，饶了我吧。\n',
            '哪有这么简单就能逃狱的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_065C')
    def lambda_065C():
        CameraMove(-146150, 0, -10, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_065C)

    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    Sleep(600)

    CreateThread(0x0102, 0x01, 0x00, 0x0005)
    Sleep(600)

    CreateThread(0x0107, 0x01, 0x00, 0x0006)
    Sleep(600)

    CreateThread(0x010B, 0x01, 0x00, 0x0008)
    Sleep(600)

    CreateThread(0x0106, 0x01, 0x00, 0x0007)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020091201V#012F这里……\n',
            '看来是地牢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010091202V#501F嗯，和哈肯大门相比，\n',
            '要塞地牢的规模要大多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_071F')
    def lambda_071F():
        CameraMove(-142480, 0, -140, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_071F)

    @scena.Lambda('lambda_0737')
    def lambda_0737():
        OP_6C(13000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0737)

    @scena.Lambda('lambda_0747')
    def lambda_0747():
        CameraSetDistance(3170, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_0747)

    @scena.Lambda('lambda_0757')
    def lambda_0757():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0757')

    DispatchAsync2(0x0107, 0x0001, lambda_0757)

    @scena.Lambda('lambda_0768')
    def lambda_0768():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0768')

    DispatchAsync2(0x0102, 0x0001, lambda_0768)

    @scena.Lambda('lambda_0779')
    def lambda_0779():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0779')

    DispatchAsync2(0x010B, 0x0001, lambda_0779)

    @scena.Lambda('lambda_078A')
    def lambda_078A():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_078A')

    DispatchAsync2(0x0106, 0x0001, lambda_078A)

    @scena.Lambda('lambda_079B')
    def lambda_079B():
        ChrWalkTo(0x00FE, -142670, 0, -2600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_079B)

    Sleep(100)

    @scena.Lambda('lambda_07BB')
    def lambda_07BB():
        ChrWalkTo(0x00FE, -141770, 0, -3520, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_07BB)

    Sleep(300)

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        ChrWalkTo(0x00FE, -142340, 0, -4140, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_07DB)

    @scena.Lambda('lambda_07F6')
    def lambda_07F6():
        ChrWalkTo(0x00FE, -143790, 0, -4480, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_07F6)

    Sleep(200)

    @scena.Lambda('lambda_0816')
    def lambda_0816():
        ChrWalkTo(0x00FE, -143830, 0, -3490, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_0816)

    WaitForThreadExit(0x0101, 0x0002)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091203V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090091204V#213F#5P啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0885')
    def lambda_0885():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0885')

    DispatchAsync2(0x0101, 0x0001, lambda_0885)

    @scena.Lambda('lambda_0896')
    def lambda_0896():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0896')

    DispatchAsync2(0x0107, 0x0001, lambda_0896)

    @scena.Lambda('lambda_08A7')
    def lambda_08A7():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_08A7')

    DispatchAsync2(0x0102, 0x0001, lambda_08A7)

    @scena.Lambda('lambda_08B8')
    def lambda_08B8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_08B8')

    DispatchAsync2(0x010B, 0x0001, lambda_08B8)

    @scena.Lambda('lambda_08C9')
    def lambda_08C9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_08C9')

    DispatchAsync2(0x0106, 0x0001, lambda_08C9)

    ChrTalk(
        0x0101,
        (
            '#0010091205V#501F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x0008)

    ChrTalk(
        0x0101,
        (
            '#005F#1K#3S啊啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0090091207V#214F#1K#3S#5P啊啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    Sleep(500)

    OP_56(0x01)
    OP_59()
    SetChrFlags(0x0009, 0x0004)
    ChrWalkTo(0x0009, -141310, 0, 1010, 6000, 0x00)
    SetChrDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#0290091208V#201F是、是你们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000A, 0x0004)
    ChrWalkTo(0x000A, -140160, 0, -530, 5000, 0x00)
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '#0300091209V#192F那时候的小鬼！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091210V#014F该说什么好呢……\n',
            '真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091211V#002F是吗……\n',
            '原来你们被关在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091212V#003F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091213V#506F嗯，那个，还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090091214V#214F#5P哼、哼……\n',
            '少来假惺惺地可怜我们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090091215V你这个只会耍棍棒的蠢女人！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091216V#007F不好意思……\n',
            '你说什么我都不会生气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091217V如果能让你觉得好过点的话，\n',
            '随便怎么骂好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090091218V#216F#5P气、气死人啦～！\n',
            '你在说什么不痛不痒的话啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091219V#052F喂喂。\n',
            '你们认识这帮家伙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091220V#010F他们是卡普亚空贼团……\n',
            '劫持定期船『林德号』的犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091221V#103F哦，是传说中的空贼啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091222V听说你们拥有性能相当高的飞艇。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091223V#101F听说是帝国制造的，\n',
            '能不能告诉我一下规格啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290091224V#202F啊、啊啊……\n',
            '最高时速可是能达到２３００塞尔矩呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290091225V#201F喂，老头。\n',
            '为什么我要回答这些啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091226V#102F什么嘛，真小气～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091227V#067F哎呀，爷爷啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091228V现在好像不是问这个的场合吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300091229V#190F等、等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300091230V说起来……\n',
            '你们这些游击士怎会在这里的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300091231V难道说刚才的警报声……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091232V#509F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091233V#015F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091234V#100F…………唔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091235V#562F…………啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091236V#053F……那么，我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EBA')
    def lambda_0EBA():
        CameraMove(-143280, 0, 2210, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0EBA)

    @scena.Lambda('lambda_0ED2')
    def lambda_0ED2():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0ED2)

    CreateThread(0x0106, 0x01, 0x00, 0x000D)
    CreateThread(0x010B, 0x01, 0x00, 0x000B)
    CreateThread(0x0102, 0x01, 0x00, 0x000A)
    CreateThread(0x0107, 0x01, 0x00, 0x000C)
    CreateThread(0x0101, 0x01, 0x00, 0x0009)
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#0090091237V#214F啊，想蒙混过去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290091238V#201F入侵者就是你们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0300091239V#196F拜、拜托～！\n',
            '把我们也放出去啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_24(0x00AC, 0x46)
    CameraMove(-24930, 0, 38220, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010B, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    SetChrPos(0x0101, -25930, 0, 36130, 0)
    SetChrPos(0x0102, -24890, 0, 36720, 315)
    SetChrPos(0x010B, -26310, 0, 37690, 135)
    SetChrPos(0x0107, -25050, 0, 38100, 225)
    SetChrPos(0x0106, -25740, 0, 38770, 180)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0107, 0)
    SetChrSubChip(0x0106, 0)
    SetChrSubChip(0x010B, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010091240V#007F呼……\n',
            '真是吓了一跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091241V#003F对了……\n',
            '他们也是和那些黑衣人一伙的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091242V为什么会被理查德上校关起来……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091243V#013F#2P他们可能只是被上校利用了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091244V或许卢安的戴尔蒙市长也是……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091245V#551F嘁，就算如此，\n',
            '我们也没必要同情他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091246V#057F浪费了这么多时间，\n',
            '快找其他可以逃脱的路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0044, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x11A2
@scena.Code('func_04_11A2')
def func_04_11A2():
    ChrWalkTo(0x00FE, -146510, 1000, 3950, 4000, 0x00)
    ChrWalkTo(0x00FE, -146280, 0, -2750, 4000, 0x00)
    ChrWalkTo(0x00FE, -145080, 0, -2750, 2000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0005 offset: 0x11E6
@scena.Code('func_05_11E6')
def func_05_11E6():
    ChrWalkTo(0x00FE, -146510, 1000, 3950, 3000, 0x00)
    ChrWalkTo(0x00FE, -146140, 0, -3690, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0x1216
@scena.Code('func_06_1216')
def func_06_1216():
    ChrWalkTo(0x00FE, -146510, 1000, 3950, 3000, 0x00)
    ChrWalkTo(0x00FE, -146080, 0, -2720, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0007 offset: 0x1246
@scena.Code('func_07_1246')
def func_07_1246():
    ChrWalkTo(0x00FE, -146510, 1000, 3950, 3000, 0x00)
    ChrWalkTo(0x00FE, -147240, 0, -2250, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0008 offset: 0x1276
@scena.Code('func_08_1276')
def func_08_1276():
    ChrWalkTo(0x00FE, -146510, 1000, 3950, 3000, 0x00)
    ChrWalkTo(0x00FE, -147320, 0, -3340, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0009 offset: 0x12A6
@scena.Code('func_09_12A6')
def func_09_12A6():
    Sleep(500)

    Sleep(500)

    ChrWalkTo(0x00FE, -146450, 0, -3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -147010, 1000, 3760, 3000, 0x00)
    ChrWalkTo(0x00FE, -150200, 3000, 3950, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x12ED
@scena.Code('func_0A_12ED')
def func_0A_12ED():
    Sleep(500)

    Sleep(500)

    Sleep(500)

    Sleep(500)

    Sleep(300)

    ChrWalkTo(0x00FE, -146450, 0, -3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -147010, 1000, 3760, 3000, 0x00)
    ChrWalkTo(0x00FE, -150200, 3000, 3950, 3000, 0x00)

    Return()

# id: 0x000B offset: 0x1343
@scena.Code('func_0B_1343')
def func_0B_1343():
    Sleep(500)

    ChrWalkTo(0x00FE, -146450, 0, -3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -147010, 1000, 3760, 3000, 0x00)
    ChrWalkTo(0x00FE, -150200, 3000, 3950, 3000, 0x00)

    Return()

# id: 0x000C offset: 0x1385
@scena.Code('func_0C_1385')
def func_0C_1385():
    Sleep(500)

    Sleep(500)

    Sleep(500)

    ChrWalkTo(0x00FE, -146450, 0, -3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -147010, 1000, 3760, 3000, 0x00)
    ChrWalkTo(0x00FE, -150200, 3000, 3950, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x13D1
@scena.Code('func_0D_13D1')
def func_0D_13D1():
    ChrWalkTo(0x00FE, -146450, 0, -3080, 3000, 0x00)
    ChrWalkTo(0x00FE, -147010, 1000, 3760, 3000, 0x00)
    ChrWalkTo(0x00FE, -150200, 3000, 3950, 3000, 0x00)

    Return()

# id: 0x000E offset: 0x140E
@scena.Code('func_0E_140E')
def func_0E_140E():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 5, 0x56D)),
            Expr.Return,
        ),
        'loc_14A6',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1461',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091265V#054F不能走这边！\n',
            '赶快顺着刚才的叫声去看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A3')

    def _loc_1461(): pass

    label('loc_1461')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050091266V#054F不能走这边！\n',
            '赶快顺着刚才的叫声去看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A3(): pass

    label('loc_14A3')

    Jump('loc_1580')

    def _loc_14A6(): pass

    label('loc_14A6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1519',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091267V#050F总之不要再去地牢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091268V让那些家伙闹起来就糟了。\n',
            '还是找找其它的逃跑路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1580')

    def _loc_1519(): pass

    label('loc_1519')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050091269V#050F喂，别再去地牢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091270V让那些家伙闹起来就糟了。\n',
            '赶快找找其它的逃跑路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1580(): pass

    label('loc_1580')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000F offset: 0x159C
@scena.Code('func_0F_159C')
def func_0F_159C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 1, 0x571)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 4, 0x56C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 5, 0x56D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_194C',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00AD, 5, 0x56D))
    OP_28(0x0044, 0x01, 0x0400)

    ChrTalk(
        0x000B,
        (
            '#4190091247V喂，找到了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x000B, 0)
    ChrTurnDirection(0x0001, 0x000B, 0)
    ChrTurnDirection(0x0002, 0x000B, 0)
    ChrTurnDirection(0x0003, 0x000B, 0)
    ChrTurnDirection(0x0004, 0x000B, 0)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0004, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#4190091248V还没有，\n',
            '兵营那边都找过了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4190091249V监视塔也无异常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4190091250V……那么只剩下\n',
            '这个司令部里面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#4190091251V向少校报告一下，\n',
            '然后进行地毯式搜索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091252V#005F不妙！\n',
            '好像朝这边来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091253V#057F可恶……\n',
            '这里就是死路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091254V#012F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0620091255V过来！这边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0004, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0000, 0x000C, 0)
    ChrTurnDirection(0x0001, 0x000C, 0)
    ChrTurnDirection(0x0002, 0x000C, 0)
    ChrTurnDirection(0x0003, 0x000C, 0)
    ChrTurnDirection(0x0004, 0x000C, 0)

    ChrTalk(
        0x0101,
        (
            '#0010091256V#004F刚才的声音，听到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091257V#065F嗯、嗯……\n',
            '好像是说来这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0620091258V……没时间了，\n',
            '你们不想被抓吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091259V#102F好像不是错觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091260V#054F没办法了！\n',
            '死马当活马医吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1A8E')

    def _loc_194C(): pass

    label('loc_194C')

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1998',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091261V#005F士兵们要来了！\n',
            '要快去传来声音的方向才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A73')

    def _loc_1998(): pass

    label('loc_1998')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19E0',
    )

    ChrTalk(
        0x0102,
        (
            '#0020091262V#012F脚步声近了……\n',
            '去传来声音的方向看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A73')

    def _loc_19E0(): pass

    label('loc_19E0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A26',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091263V#057F这边不妙……\n',
            '去传来声音的方向一探吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A73')

    def _loc_1A26(): pass

    label('loc_1A26')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A73',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091264V#065F士兵们快过来了……\n',
            '要赶快去传来声音的方向才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A73(): pass

    label('loc_1A73')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_1A8E(): pass

    label('loc_1A8E')

    Return()

# id: 0x0010 offset: 0x1A8F
@scena.Code('func_10_1A8F')
def func_10_1A8F():
    EventBegin(0x00)
    CameraMove(21440, 0, 108290, 0)
    SetChrPos(0x000C, 20330, 0, 120850, 0)
    SetChrPos(0x0101, 21240, 0, 106790, 0)
    SetChrPos(0x0102, 20030, 0, 106050, 0)
    SetChrPos(0x0107, 21530, 0, 105630, 0)
    SetChrPos(0x0106, 21050, 0, 104420, 0)
    SetChrPos(0x010B, 20280, 0, 104880, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0620091271V快！\n',
            '就这样一直走进来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091272V#004F约修亚，这个声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091273V#012F啊……\n',
            '我记得这声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x1B7D
@scena.Code('func_11_1B7D')
def func_11_1B7D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 7, 0x56F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C30',
    )

    SetScenaFlags(ScenaFlag(0x00AD, 7, 0x56F))
    SetChrPos(0x000C, 21160, 0, 159230, 0)
    OP_1C(0x12, 0x00, 0xFFFF)
    EventBegin(0x00)
    CameraMove(21080, 0, 158340, 1000)

    ChrTalk(
        0x000C,
        (
            '#0620091274V来，快进来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091275V#050F喂喂，这个房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091276V#100F唔，不知他打算怎样，\n',
            '现在唯有进去一看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    OP_71(0x0012, 0x0010)

    def _loc_1C30(): pass

    label('loc_1C30')

    Return()

# id: 0x0012 offset: 0x1C31
@scena.Code('func_12_1C31')
def func_12_1C31():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 6, 0x56E)),
            Expr.Return,
        ),
        'loc_1CEA',
    )

    SetScenaFlags(ScenaFlag(0x00AD, 7, 0x56F))
    SetChrPos(0x000C, 21160, 0, 159230, 0)
    OP_1C(0x12, 0x00, 0xFFFF)
    EventBegin(0x00)
    CameraMove(21080, 0, 158340, 1000)

    ChrTalk(
        0x000C,
        (
            '#0620091274V来，快进来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091275V#052F喂喂，这个房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0540091276V#102F唔，不知他打算怎样，\n',
            '现在唯有进去一看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    OP_71(0x0012, 0x0010)
    OP_64(0x00, 0x0001)

    Jump('loc_1D39')

    def _loc_1CEA(): pass

    label('loc_1CEA')

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    def _loc_1D39(): pass

    label('loc_1D39')

    Return()

# id: 0x0013 offset: 0x1D3A
@scena.Code('func_13_1D3A')
def func_13_1D3A():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
